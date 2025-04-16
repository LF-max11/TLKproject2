# Name:         Unique Words in a Sentence (08_Unique Words in a Sentence.py)
# Purpose:      To Extract unique words from a sentence using a set
# Author:       LF
# Created:      08-April-2025
# Updated:      08-April-2025
#-----------------------------------------------------------------------------

print("Start")
#Given a sentence
sentence = "The quick brown fox jumps over the lazy dog"
# Split sentence into words and convert to a set
unique_words = set(sentence.split())
# Print unique words
print(unique_words)