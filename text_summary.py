import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    # print(stopwords)

    nlp = spacy.load('en_core_web_sm') 
    # storing the smallest module
    doc = nlp(rawdocs)
    # print(doc)
    tokens = [token.text for token in doc ]
    # print(tokens)

    word_freq={}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text]=1
            else:
                word_freq[word.text]+=1

    # print(word_freq)

    max_freq = max(word_freq.values())
    # print(max_freq)

    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq
    # normalised freq 

    # print(word_freq)

    sent_tokens = [sent for sent in doc.sents]
    # print(sent_tokens)

    sent_score = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_score.keys():
                    sent_score[sent] = word_freq[word.text]
                else:
                    sent_score[sent] += word_freq[word.text]

    # print(sent_score)

    select_len = int(len(sent_tokens) * 0.3)
    # print(select_len)

    summary = nlargest(select_len,sent_score,key = sent_score.get)
    # print(summary)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    print("SUMMARY OF THE TEXT IS: ")
    # print(summary)
    # print("Length of original text ", len(text.split(' ')))
    # print("Length of summary text ", len(summary.split(' ')))

    return summary,doc,len(tokens),len(summary.split(' '))

if __name__ == "__main__":
    
    text = input("Enter the text")
    smmary, origi, lenor, l = summarizer(text)
    print(smmary)
