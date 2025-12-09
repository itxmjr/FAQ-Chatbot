from typing import List, Tuple

from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer

from .preprocessing import preprocess_corpus


def build_tfidf_vectorizer(
    questions: List[str],
    max_features: int | None = None
) -> Tuple[TfidfVectorizer, csr_matrix]:
    """
    Preprocess FAQ questions and fit a TF-IDF vectorizer on them.

    Returns:
        vectorizer: fitted TfidfVectorizer
        faq_matrix: sparse matrix of shape (n_faqs, n_features)
    """
    preprocessed_questions = preprocess_corpus(questions)

    vectorizer = TfidfVectorizer(
        max_features=max_features,
        ngram_range=(1, 2),  # unigrams + bigrams help matching paraphrases
    )
    faq_matrix = vectorizer.fit_transform(preprocessed_questions)

    return vectorizer, faq_matrix


def vectorize_query(query: str, vectorizer: TfidfVectorizer) -> csr_matrix:
    """
    Preprocess and vectorize a single user query using an existing TF-IDF vectorizer.
    """
    preprocessed_query = preprocess_corpus([query])
    query_vector = vectorizer.transform(preprocessed_query)
    return query_vector