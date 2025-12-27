from src.data_loader import load_faqs, get_questions_and_answers

def test_load_faqs_returns_list():
    faqs = load_faqs()
    assert isinstance(faqs, list)
    assert len(faqs) > 0

    item = faqs[0]
    assert "question" in item
    assert "answer" in item


def test_get_questions_and_answers():
    faqs = load_faqs()
    questions, answers = get_questions_and_answers(faqs)

    assert len(questions) == len(answers) == len(faqs)
    assert isinstance(questions[0], str)
    assert isinstance(answers[0], str)