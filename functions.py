import pandas as pd
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Returns the most common words in each tweet
def mostCommonWords(words, top):
    stop_words = set(stopwords.words('english'))
    manual_removal = set(['http', 'https', 'amp', 'a', 'and', 'but', 'because', 'it', "n't", 'or', 'so', 'rt', 'the'])
    filtered_words = [word for word in words if not word in stop_words]
    final_words = []
    for word in filtered_words:
        if re.match('[a-zA-Z]+', word) and word.lower() not in manual_removal:
            final_words.append(word.lower())
    word_frequencies = nltk.FreqDist(final_words)
    return word_frequencies.most_common(top)

# Adds top traits to frames
def addToFrame(label, data):
    pwords = []
    pfreqs = []
    for x, y in data:
        pwords.append(x)
        pfreqs.append(y)
    return pd.DataFrame({label: pwords, 'Frequency': pfreqs})

# Returns Polarity of Each Tweet in DataFrame format
def polarizeFrame(x, s):
    sia = SentimentIntensityAnalyzer()
    pos = []
    neg = []
    neu = []
    c = []
    for i in range(0, s.size):
        scores = sia.polarity_scores(str(s.loc[i]))
        pos.append(scores.get("pos"))
        neg.append(scores.get("neg"))
        neu.append(scores.get("neu"))
        c.append(scores.get("compound"))
    return pd.DataFrame({"Date": x, "Text": s, "Positivity": pos, "Negativity": neg, "Neutrality": neu, "Compound": c})

# Returns a list of all the hashtags in every tweet
def hashTagPhrases(tweets_Data, top):
    hashList = []
    nan = []
    lst = []
    for i in range(0, tweets_Data.size):
        try:
            if '#' in word_tokenize(tweets_Data.loc[i]):
                phrase = re.findall('#[a-z]\S*', tweets_Data.loc[i])
                hashList.append(phrase)
        except:
            nan.append(tweets_Data.loc[i])
    while [] in hashList:
        hashList.remove([])
    for i in range(0, len(hashList)):
        for a in range(0, len(hashList[i])):
            lst.append(hashList[i][a])
    hashFreq = nltk.FreqDist(lst)
    mostHashtagList = hashFreq.most_common(top)
    return mostHashtagList

# Returns a list of all the mentions in every tweet
def mostMentions(tweets_Data, top):
    atList = []
    nan = []
    atfnlList = []
    for i in range(0, tweets_Data.size):
        try:
            if '@' in word_tokenize(tweets_Data.loc[i]):
                phrase = re.findall('@[a-z]\S*', tweets_Data.loc[i])
                atList.append(phrase)
        except:
            nan.append(tweets_Data.loc[i])
    while [] in atList:
        atList.remove([])
    for i in range(0, len(atList)):
        for a in range(0, len(atList[i])):
            atfnlList.append(atList[i][a])
    atfnlList = [s.strip(':') for s in atfnlList]    
    mentionFreq = nltk.FreqDist(atfnlList)
    mostMentionList = mentionFreq.most_common(top)
    return mostMentionList
