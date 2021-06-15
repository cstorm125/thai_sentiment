# !/usr/bin/env python

from distutils.core import setup
setup(
    name='thai_sentiment',
    packages=[],
    version='0.1.0',
    description='The naive sentiment classification function basedon NBSVM trained on wisesight_sentiment',
    author='cstorm125',
    license='Apache 2.0',
    author_email='cebril@gmail.com',
    url='https://github.com/cstorm125/thai_sentiment',
    keywords=['sentiment analysis', 'thai', 'nlp'],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: Thai',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
)