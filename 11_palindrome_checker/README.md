from solution_optimized import summarize

text = "Python is great. Python is easy to learn. Python is powerful."
summary = summarize(text, 2)

assert "Python" in summary
print("Text summarizer tests passed")
