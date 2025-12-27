import re
from collections import Counter

def summarize(text: str, max_sentences=3) -> str:
    sentences = re.split(r'(?<=[.!?]) +', text)
    words = re.findall(r'\w+', text.lower())
    frequency = Counter(words)

    sentence_scores = {}
    for sentence in sentences:
        sentence_scores[sentence] = sum(
            frequency[word.lower()]
            for word in re.findall(r'\w+', sentence)
        )

    ranked = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    return " ".join(ranked[:max_sentences])
