from solution_optimized import summarize

text = "Python is easy. Python is powerful. Python is popular."
summary = summarize(text, 2)
assert "Python" in summary
print("Text summarizer tests passed")
