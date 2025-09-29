from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from src.llm_client import get_llm

def analyze_sentiment(text: str) -> str:
    llm = get_llm()

    prompt = PromptTemplate(
        input_variables=["text"],
        template=(
            "You are a sentiment analysis model. "
            "Classify the sentiment of the following text as the closest human emotion.\n\n"
            "Text: {text}\n"
            "Sentiment:"
        )
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({"text": text})

    return result.strip()
