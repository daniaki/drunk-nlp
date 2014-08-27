''' Author  : Daniel Esposito
    Date    : 25/8/14
    Pupose  : Defines a class representing a tweet with fields
              userId, tweetId and bodyText
'''
from tokenise import *
from nGram import *

class Tweet:
    #Houses user, tweet id and text and total tweets in memory
    tweetCount = 0

    def __init__(self, userId, tweetId, tweetText):
        self.userId = str(userId)
        self.tweetId = str(tweetId)
        self.tweetText = str(tweetText)
        self.cleanText = cleanTweet(str(tweetText))
        Tweet.tweetCount += 1

    def joinFields(self):
        fullTweet = self.userId + '\t' + self.tweetId + '\t' + self.tweetText
        return fullTweet

    def compareUser(self, tweet):
        if self.userId == tweet.userId:
            return True
        else:
            return False

    def compareFull(self, tweet):
        if self.userId == tweet.userId and self.tweetId == tweet.tweetId and self.tweetText == tweet.tweetText:
            return True
        else:
            return False
