from src.sentiment_chain import analyze_sentiment

def test_positive_sentiment():
    text = "I absolutely love this product!"
    result = analyze_sentiment(text)
    assert "Positive" in result

def test_negative_sentiment():
    text = "This is the worst experience ever."
    result = analyze_sentiment(text)
    assert "Negative" in result

def test_neutral_sentiment():
    text = "The event will take place tomorrow."
    result = analyze_sentiment(text)
    assert "Neutral" in result