# `thai_sentiment`
The naive sentiment classification function based on NBSVM trained on [wisesight_sentiment](https://huggingface.co/datasets/wisesight_sentiment)

## วิธีติดตั้ง

```
pip install thai_sentiment==0.1.3
```

## วิธีใช้

```
from thai_sentiment import get_sentiment

get_sentiment('ร้านนี้บรรยากาศดีนะครับ')
> ('pos', #pos แปลว่า เป็นบวก
 {'pos': 0.33864993351079425,
  'neu': 0.28699790627796756,
  'neg': 0.07578396636250984})
  
get_sentiment('ร้านนี้อาหารอย่างแย่')
> ('neg', #neg แปลว่า เป็นลบ
 {'pos': 0.07848318054147058,
  'neu': 0.28609131356977374,
  'neg': 0.3279735800256706})
  
get_sentiment('ร้านนี้อยู่บางรัก')
> ('neu', #neu แปลว่า เฉยๆ
 {'pos': 0.23328174158421325,
  'neu': 0.6859672540205807,
  'neg': 0.024412368023402797})
```

## Notes

Library นี้สร้างขึ้นจากการใช้โมเดล NBSVM ที่เทรนด้วยข้อมูล [wisesight_sentiment](https://huggingface.co/datasets/wisesight_sentiment) ซึ่งจะเห็นว่าได้ผลดีพอประมาณ (Micro-averaged F1 72.03 vs 76.19 จาก [WangchanBERTa โมเดลที่ดีที่สุด](https://medium.com/airesearch-in-th/wangchanberta-%E0%B9%82%E0%B8%A1%E0%B9%80%E0%B8%94%E0%B8%A5%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%A1%E0%B8%A7%E0%B8%A5%E0%B8%9C%E0%B8%A5%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B9%84%E0%B8%97%E0%B8%A2%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%83%E0%B8%AB%E0%B8%8D%E0%B9%88%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%81%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%AA%E0%B8%B8%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%82%E0%B8%93%E0%B8%B0%E0%B8%99%E0%B8%B5%E0%B9%89-d920c27cd433) เหมาะสำหรับคนที่ไม่อยากเทรนโมเดลอะไรเลย แค่อยากเรียก function `get_sentiment` แล้วได้ว่าข้อความเป็น `บวก`, `กลาง`, `ลบ` 

|              | Micro-averaged F1   |
|--------------|---------------------|
| NBSVM        | 72.03               |
| ULMFit       | 70.95               |
| XLMR         | 73.57               |
| mBERT        | 70.05               |
| WanchanBERTa | 76.19               |

แน่นอนว่าโมเดล machine learning ทุกโมเดลทำงานได้ดีใน domain เฉพาะของมัน เพราะงั้นถ้าคุณอยากได้โมเดลดีๆเราก็แนะนำให้ไปเทรนโมเดลบนชุดข้อมูลของคุณเองตาม[โพสนี้](https://www.facebook.com/groups/thainlp/permalink/892456407802517/)มากกว่าที่จะมานั่งเรียก function ที่เทรนจากชุดข้อมูลอื่นแบบนี้

