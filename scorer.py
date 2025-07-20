import math

def estimate_entropy(tokens: list) -> float:
    """
    Estimates entropy (uncertainty) from token probability distribution
    """
    distribution = {t: tokens.count(t)/len(tokens) for t in set(tokens)}
    entropy = -sum(p * math.log2(p) for p in distribution.values())
    return entropy

def score_confidence(entropy: float, threshold: float = 3.5) -> float:
    """
    Convert entropy to confidence score (0–1)
    """
    return round(max(0, 1 - (entropy / threshold)), 2)

