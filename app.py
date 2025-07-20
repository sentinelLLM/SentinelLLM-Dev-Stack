import streamlit as st
from promptshield.scanner import scan_prompt
from sanitizer.sanitizer import sanitize_output
from hallucinationmeter.scorer import estimate_entropy, score_confidence

st.title("SentinelLLM Prompt Safety Tester")

prompt = st.text_area("Enter your prompt")

if prompt:
    score, threat = scan_prompt(prompt)
    entropy = estimate_entropy(prompt.split())
    confidence = score_confidence(entropy)
    sanitized = sanitize_output(prompt)

    st.write(f"🧠 Risk Score: `{score}` ({threat})")
    st.write(f"🔍 Confidence Level: `{confidence}`")
    st.write(f"🧼 Sanitized Output: `{sanitized}`")

