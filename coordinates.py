#Task 2.1
import math

cor1 = (0,0)
cor2 = (0,3)
cor3 = (3,3)

coords = (cor1,cor2,cor3)

def distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def midpoint(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return ((x1 + x2) / 2, (y1 + y2) / 2)

print(f"distance of cor1 and cor2{distance(cor1,cor2)}")
print(f"midpoint of cor2 and cor 3{midpoint(cor2,cor3)}")
print("")

#Task 2.2
from collections import Counter
import re

text = "Python is a programming language. Python is easy to learn. Python is powerful."

words = re.findall(r'\b\w+\b', text.lower())

unique_words = set(words)

total_words = len(words)
unique_word_count = len(unique_words)

word_counts = Counter(words)
most_common_words = word_counts.most_common(2)
print("Original Text:")
print(text)
print("\nWords:")
print(words)
print("\nUnique Words:")
print(unique_words)
print("\nTotal Words:", total_words)
print("Unique Word Count:", unique_word_count)
print("\nMost Common Words:")
for word, count in most_common_words:
    print(f"{word}: {count}")
