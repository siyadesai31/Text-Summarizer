import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = input("Enter the text")

stopwords = list(STOP_WORDS)
# print(stopwords)

nlp = spacy.load('en_core_web_sm') 
# storing the smallest module
doc = nlp(text)
# print(doc)
tokens = [token.text for token in doc ]
# print(tokens)
