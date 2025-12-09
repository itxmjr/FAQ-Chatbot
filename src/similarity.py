from typing import Tuple

import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity


def find_best_faq_match(
    query_vector: csr_matrix,
    faq_matrix: csr_matrix
) -> Tuple[int, float]:
    """
    Compute cosine similarity between the user query and all FAQ vectors.

    Returns:
        best_index: index of the most similar FAQ
        best_score: cosine similarity score (0.0 - 1.0)
    """
    # cosine_similarity returns shape (1, n_faqs)
    similarities = cosine_similarity(query_vector, faq_matrix)[0]

    best_index = int(np.argmax(similarities))
    best_score = float(similarities[best_index])

    return best_index, best_score