from src.preprocessing import preprocess_text, preprocess_corpus

def test_preprocess_text_basic():
    text = "How do I create a NEW account?"
    tokens = preprocess_text(text)

    assert isinstance(tokens, list)
    assert "account" in tokens

    assert "how" not in tokens
    assert "do" not in tokens
    assert "i" not in tokens


def test_preprocess_corpus_returns_strings():
    texts = ["Hello, world!", "This is a test."]
    processed = preprocess_corpus(texts)
    assert len(processed) == 2
    assert all(isinstance(p, str) for p in processed)