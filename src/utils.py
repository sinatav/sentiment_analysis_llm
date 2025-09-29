def clean_text(text: str) -> str:
    """Basic cleaning of input text."""
    return text.strip().replace("\n", " ")
