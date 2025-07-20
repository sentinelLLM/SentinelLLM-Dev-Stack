import json
import random
from promptshield.scanner import scan_prompt

# Load attack payloads
def load_payloads(filepath: str = "payloads.json") -> list:
    with open(filepath, "r") as f:
        return json.load(f)

def run_simulation(llm_function, payloads: list):
    results = []
    for payload in payloads:
        prompt = payload["prompt"]
        expected = payload["category"]
        risk_score, threat_type = scan_prompt(prompt)
        response = llm_function(prompt)  # Stubbed or real LLM call
        results.append({
            "prompt": prompt,
            "expected": expected,
            "score": risk_score,
            "detected": threat_type,
            "llm_response": response
        })
    return results

