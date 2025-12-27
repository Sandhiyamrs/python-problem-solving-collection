from solution_optimized import summarize

text = "Python is easy. Python is powerful. Python is widely used."
summary = summarize(text, 2)

assert "Python" in summary
print("Text Summarizer tests passed")
