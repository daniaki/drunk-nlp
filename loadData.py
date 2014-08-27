''' Author  : Daniel Esposito
    Date    : 25/8/14
    Pupose  : File to open tweet, common words and query data. Default input
              files are the small variants and should be placed in data folder
'''
import re
import sys
import logging
#import tweet

#Set-up debugging logger
logging.basicConfig(filename='filedebug.log',level=logging.DEBUG)

#grammar, special char pattern match
grammar = r'.,!{}@#$%^&*()_+=><?|'
path = './data/'

# Purpose: Create a new file or open exisiting output file
# @param1: Name of file to create
# @param2: Mode to open file with
# @return: fd for new file/existing file
def openFile(filePath, mode):
    try:
        fd = open(filePath, mode, encoding="utf-8")
        logging.debug("File: " + filePath + " opened successfully")
        return fd
    except Exception:
        logging.debug('File: ' + filePath + " not found or could not be opened")
        print("IOError, see log for details")
        sys.exit()

# Purpose: Takes a path to file in root directory
# @param1: path to tweet data
# @return: Array of lower case, special char free tweets
#          Each array index has the form [user_id, tweet_id, tweet_text]
def loadTweetData(filePath = path + "training_set_tweets_small.txt"):
    data = openFile(filePath, 'r')
    hasTimeStamp = lambda x: re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', x)
    hasUID = lambda x: re.search(r'^\d{2,}\t\d{2,}\t', x)
    tweets = []
    line = data.readline()
    try:
        while line:
            #assuming lines with not data stamp are imcomplete
            if not hasTimeStamp(line):
                pos = data.tell()
                nextLine = data.readline()
                if not hasUID(nextLine):
                    while not hasUID(nextLine):
                        pos = data.tell()
                        line += " " + nextLine
                        nextLine = data.readline()
                data.seek(pos)
            #strip \n and \t and split into an array
            line = re.sub(r'[\r\n]', "", line)
            tweet = line.split('\t')
            tweets.append(tweet)
            line = data.readline()
        return tweets
    except UnicodeDecodeError:
        logging.debug("Unicode error while parsing tweet file")
        print("Parsing error in preprocess.py, see log for details")
        sys.exit()
        
# Purpose: Takes a path to file in root directory
# @param1: path to query data
# @return: List of lower case, special char free queries
def loadQueryData(filePath = path + "US_small.txt"):
    data = openFile(filePath, 'r')
    locations = []
    asciiPos = 2
    try:
        for line in data:
            place = line.split('\t')[asciiPos].lower()
            place = re.sub(grammar, "", place)
            locations.append(place)
        return locations
    except UnicodeDecodeError:
        logging.debug("Unicode error while parsing query file")
        print("Parsing error in preprocess.py, see log for details")
        sys.exit()
        
# Purpose: A list of common English stop words to check against
# @return: list of lower case, grammar free words from txt file
def loadCommon():
    commonWords = openFile(path + "stopwords.txt", 'r').read()
    try:
        filterWords= lambda x: re.sub(grammar, "", x)
        commonWords = list(map(filterWords, commonWords.split()))
        return commonWords
    except UnicodeDecodeError:
        logging.debug("Unicode error while parsing stopwords file")
        print("Parsing error in preprocess.py, see log for details")
        sys.exit()
      
# Purpose: Wrapper to write a tweet to output file
# @param1: Name of file to write to
# @param2: tweet object to output
def writeTweet(filePath, tweet, mode):
    if mode not in ['w','w+', 'a', 'a+']:
        logging.debug("Tried to write tweet data using read mode")
        print("Attempted to use incorrect mode for file writing, \
                see log for details")
        sys.exit()
    text = tweet
    fd = openFile(filePath, mode)
    try:
        fd.write(text)
        fd.close()
    except Exception:
        logging.debug("Error while writing to output file")
        print("Write error in writeTweet(...), see log for details")
        sys.exit()
