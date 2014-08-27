from loadData import *
from tweet import *
from nGram import *
from editDistance import *
from tokenise import *
import os, sys, re

def main():
    #load sample query data as list
    queries = loadQueryData()
    minQueryLen = len(min(queries, key=len))
    print(minQueryLen)

    #load sample tweet data in the specified format
    tweets = loadTweetData()
    tweetObjArr = []
    for tweet in tweets:
        #class does the cleaning and ngram building
        tweetObjArr.append(Tweet(tweet[0], tweet[1], tweet[2]))
        print(Tweet(tweet[0], tweet[1], tweet[2]).joinFields())
        print(Tweet(tweet[0], tweet[1], tweet[2]).cleanText)

    #for each tweet
        #if tweet tokens max size less than minQueryLen
        #discard tweet
        #else test each query against tokens in tweet text
        #if match, add tweet id to ditionary under query key

    #write all keys and their values to output
        
#run main
main()
