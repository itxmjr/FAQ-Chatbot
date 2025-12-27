import json
from pathlib import Path
from typing import List, Dict, Tuple


def load_faqs(path: str = "data/faqs.json") -> List[Dict]:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"FAQ File not found at: {file_path.resolve()}")

    with file_path.open("r", encoding="utf-8") as f:
        faqs = json.load(f)

    return faqs


def get_questions_and_answers(faqs: List[Dict]) -> Tuple[List[str], List[str]]:
    questions = [item["question"] for item in faqs]
    answers = [item["answer"] for item in faqs]
    return questions, answers