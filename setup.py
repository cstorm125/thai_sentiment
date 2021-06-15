from distutils.core import setup

setup(
    name='thai_sentiment',
    packages=['thai_sentiment'],
    version='v0.1.0',  # Ideally should be same as your GitHub release tag varsion
    description='The naive sentiment classification function based on NBSVM trained on wisesight_sentiment',
    author='cstorm125',
    author_email='cebril@gmail.com',
    url='https://github.com/cstorm125/thai_sentiment',
    download_url='https://github.com/cstorm125/thai_sentiment/archive/refs/tags/v0.1.1.tar.gz',
    keywords=['sentiment analysis', 'thai', 'nlp'],
    classifiers=[],
    install_requires=[
        'pythainlp',
        'sklearn',
        'pickle',
        'scipy',
    ],
)
