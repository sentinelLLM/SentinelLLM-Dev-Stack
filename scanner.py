import re
from typing import Tuple

# Define injection patterns using OWASP-style prompts
PATTERNS = [
    r"ignore previous instructions",
    r"simulate terminal",
    r"repeat after me",
    r"you are now",
    r"system override",
    r"bypass content filter",
]

def scan_prompt(prompt: str) -> Tuple[float, str]:
    """
    Scans a prompt and returns a risk score and threat type
    """
    threat_type = "None"
    score = 0.0

    for pattern in PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            threat_type = "Prompt Injection"
            score += 0.6

    if "admin password" in prompt.lower():
        threat_type = "Privilege Escalation"
        score += 0.4

    return min(score, 1.0), threat_type

