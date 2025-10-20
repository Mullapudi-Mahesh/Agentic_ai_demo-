from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str) -> str:
    """Summarize text using Hugging Face summarizer"""
    result = summarizer(text, max_length=80, min_length=30, do_sample=False)
    return result[0]['summary_text']

def search_web(query: str) -> str:
    """Mock search function for demo"""
    return f"Search results for '{query}': AI helps automate workflows and build smart assistants."
