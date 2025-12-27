import re
from collections import Counter

def summarize(text, limit=3):
    sentences = re.split(r'(?<=[.!?]) +', text)
    words = re.findall(r'\w+', text.lower())
    freq = Counter(words)

    scored = {}
    for sentence in sentences:
        scored[sentence] = sum(freq[w.lower()] for w in re.findall(r'\w+', sentence))

    best = sorted(scored, key=scored.get, reverse=True)
    return " ".join(best[:limit])
