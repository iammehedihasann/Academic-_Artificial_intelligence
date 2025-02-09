from collections import Counter
def word_count(text):
    words = text.lower().split()
    words_counter = Counter(words)
    return dict(words_counter)

text = "apple banana apple orange banana apple orange orange banana"
word_count_dict = word_count(text)
print("Words are: ", text)
print(word_count_dict)