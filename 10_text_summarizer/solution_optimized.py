import re
from collections import Counter

def summarize(text: str, max_sentences=3) -> str:
    sentences = re.split(r'(?<=[.!?]) +', text)
    words = re.findall(r'\w+', text.lower())

    freq = Counter(words)
    sentence_scores = {}

    for sentence in sentences:
        score = sum(freq.get(word.lower(), 0) for word in re.findall(r'\w+', sentence))
        sentence_scores[sentence] = score

    summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    return " ".join(summary[:max_sentences])
