import re
from typing import List

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer



_stopwords = None
_lemmatizer = None

def get_stopwords():
    global _stopwords
    if _stopwords is None:
        _stopwords = set(stopwords.words("english"))
    return _stopwords

def get_lemmatizer():
    global _lemmatizer
    if _lemmatizer is None:
        _lemmatizer = WordNetLemmatizer()
    return _lemmatizer


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def preprocess_text(text: str) -> List[str]:
    text = clean_text(text)
    tokens = nltk.word_tokenize(text)

    stops = get_stopwords()
    lemmatizer = get_lemmatizer()

    tokens = [
        tok for tok in tokens
        if tok not in stops and not tok.isdigit()
    ]

    lemmas = [lemmatizer.lemmatize(tok) for tok in tokens]

    return lemmas


def preprocess_corpus(texts: List[str]) -> List[str]:
    return [" ".join(preprocess_text(t)) for t in texts]