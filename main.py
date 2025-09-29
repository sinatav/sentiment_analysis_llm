from src.sentiment_chain import analyze_sentiment

if __name__ == "__main__":
    text = input("Enter text to analyze sentiment: ")
    sentiment = analyze_sentiment(text)
    print(f"Sentiment: {sentiment}")
