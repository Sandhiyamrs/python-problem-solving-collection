def summarize(text, sentence_count=2):
    sentences = text.split(".")
    return ".".join(sentences[:sentence_count]) + "."
