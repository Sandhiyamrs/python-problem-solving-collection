def summarize(text):
    sentences = text.split(". ")
    return ". ".join(sentences[:2]) + "."

text = input("Enter text: ")
print("\nSummary:\n", summarize(text))
