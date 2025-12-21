sentence = input("Enter a sentence: ").lower().split()
freq = {}

for word in sentence:
    freq[word] = freq.get(word, 0) + 1

for word, count in freq.items():
    print(word, ":", count)
