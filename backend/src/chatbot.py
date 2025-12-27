import random
from typing import Tuple, Optional, List

from .data_loader import load_faqs, get_questions_and_answers
from .vectorizer import build_tfidf_vectorizer, vectorize_query
from .similarity import find_best_faq_match
from .nltk_setup import ensure_nltk_resources


class FAQChatbot:
    def __init__(
        self,
        faq_path: str = "data/faqs.json",
        min_similarity: float = 0.3,
        max_features: int | None = None,
    ) -> None:
        self.faq_path = faq_path
        self.min_similarity = min_similarity
        self.max_features = max_features

        ensure_nltk_resources()

        self.faqs = load_faqs(faq_path)
        self.questions, self.answers = get_questions_and_answers(self.faqs)

        self.vectorizer, self.faq_matrix = build_tfidf_vectorizer(
            self.questions,
            max_features=self.max_features,
        )

    def get_answer(
        self,
        user_query: str,
    ) -> Tuple[str, str, float]:
        """
        Return:
            answer: best-matching answer or fallback text
            matched_question: the FAQ question that matched best (for debugging/UX)
            score: cosine similarity score
        """
        if not user_query.strip():
            return (
                "Please ask a question.",
                "",
                0.0,
            )

        query_vec = vectorize_query(user_query, self.vectorizer)
        best_idx, best_score = find_best_faq_match(query_vec, self.faq_matrix)

        if best_score < self.min_similarity:
            # Fallback response
            return (
                "I’m not sure I have an exact answer for that. "
                "Please try rephrasing or ask about another topic.",
                "",
                best_score,
            )

        best_answer = self.answers[best_idx]
        best_question = self.questions[best_idx]
        return best_answer, best_question, best_score



    def get_categories(self) -> List[str]:
        """Return a sorted list of unique FAQ categories."""
        categories = {item.get("category", "General") for item in self.faqs}
        return sorted(list(categories))

    def get_random_questions(self, n: int = 5) -> List[str]:
        """Return a random sample of questions to guide the user."""
        if not self.questions:
            return []
        n = min(n, len(self.questions))
        return random.sample(self.questions, n)

    def get_all_faqs(self) -> List[dict]:
        """Return all FAQ items."""
        return self.faqs


# Optional: a lazy singleton for simple scripts
_default_bot: Optional[FAQChatbot] = None


def get_default_bot() -> FAQChatbot:
    global _default_bot
    if _default_bot is None:
        _default_bot = FAQChatbot()
    return _default_bot


def answer_question(user_query: str) -> str:
    """
    Simple function API for quick use:
        from src.chatbot import answer_question
    """
    bot = get_default_bot()
    answer, _, _ = bot.get_answer(user_query)
    return answer