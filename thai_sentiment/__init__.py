from typing import Tuple, List
from thai_sentiment import __file__ as thai_sentiment_file
from pathlib import Path
import os
from .architecture import NbSvmClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from pythainlp.ulmfit import process_thai
import pickle
import urllib.request


class CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if name == 'NbSvmClassifier':
            from .architecture import NbSvmClassifier
            return NbSvmClassifier
        return super().find_class(module, name)


thai_sentiment_path = Path(os.path.dirname(thai_sentiment_file))
labels = ["pos", "neu", "neg"]

MODEL_URL = "https://github.com/cstorm125/thai_sentiment/raw/main/thai_sentiment/pretrained/nbsvm_c3_l2_dual.pkl"
ENC_URL = "https://github.com/cstorm125/thai_sentiment/raw/main/thai_sentiment/pretrained/tfidf_wisesight_sentiment.pkl"
urllib.request.urlretrieve(MODEL_URL, thai_sentiment_path / 'pretrained/nbsvm_c3_l2_dual.pkl')
urllib.request.urlretrieve(ENC_URL, thai_sentiment_path / 'pretrained/tfidf_wisesight_sentiment.pkl')

with open(thai_sentiment_path / 'pretrained/tfidf_wisesight_sentiment.pkl', 'rb') as f:
    tfidf = pickle.load(f)
models = CustomUnpickler(open(thai_sentiment_path / 'pretrained/nbsvm_c3_l2_dual.pkl', 'rb')).load()


def get_sentiment(text: str)->Tuple[str, List[float]]:
    probs = {'pos': 0., 'neu': 0., 'neg': 0.}
    for i in range(len(labels)):
        probs[labels[i]] = models[i].predict_proba(tfidf.transform([text]))[:, 1][0]
    return max(probs, key=probs.get), probs
