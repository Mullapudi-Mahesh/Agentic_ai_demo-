import re

def pii_guardrail(text: str) -> bool:
    """Return False if text seems to contain PII"""
    if re.search(r"\b\d{10}\b", text):  # phone numbers
        return False
    if re.search(r"@[\w.]+", text):     # emails
        return False
    return True

def tone_guardrail(text: str) -> bool:
    """Ensure polite tone (basic demo check)"""
    bad_words = ["stupid", "idiot", "hate"]
    return not any(word in text.lower() for word in bad_words)
