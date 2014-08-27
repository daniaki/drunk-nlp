''' Author  : Daniel Esposito
    Date    : 25/8/14
    Pupose  : Functionality to tokenise string text into english
              alphabet words, lowercase and removed grammar
'''
from loadData import loadCommon
from loadData import loadTweetData
import re, os
from nltk import tokenize

# pattern match for url and non-alphabetic chars
nonAlpha = r'[^A-Za-z]?[\d]?'
url = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
commonWords = loadCommon()

# Purpose: strips any character that's not a word or digit
# @param1: word to filter
# @return: lower case word only containing a-z
def cleanToken(word):
    word = re.sub(url, ' ', word)
    return re.sub(nonAlpha, '', word).lower()

# Purpose: strips any word that's a common word
# @param1: word to check
# @return: True if so, otherwise false
def filterCommon(word):
    if word not in commonWords and len(word) > 2:
        return True
    else:
        return False
    
# Purpose: takes a string (query/tweet) and cleans grammar, spaces, etc
# @param1: tweet in the form { id (tab) ... }
# @result: List of pure latin words in lower case
def cleanTweet(tweet):
    result = map(cleanToken, tweet.split())
    result = list(filter(filterCommon, result))
    return list(result)

def test():
    x = loadTweetData()
    res = []
    for i in x:
        res.append(cleanTweet(i[2]))
    return res
