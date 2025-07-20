import re

PII_PATTERNS = {
    "email": r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
    "phone": r"\b(\+?\d{1,3})?[ -]?\(?\d{3}\)?[ -]?\d{3}[ -]?\d{4}\b",
    "name": r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b",
    "address": r"\b\d{1,4} [A-Z][a-z]+ (Street|St|Avenue|Ave|Road|Rd|Blvd)\b"
}

def sanitize_output(text: str) -> str:
    """
    Scrubs output of PII patterns with [REDACTED]
    """
    for label, pattern in PII_PATTERNS.items():
        text = re.sub(pattern, "[REDACTED]", text, flags=re.IGNORECASE)
    return text

