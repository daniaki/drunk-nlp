''' Author  : Daniel Esposito
    Date    : 25/8/14
    Pupose  : Provides functions to conduct a Set based n-gram
              comparison for document similarity measurement
'''
# Purpose: recursive algorithm to compute ngram for a list
# @param1: list to make ngram out of
# @return: Returns the n-gram as a Set object
def nGram(n, inList):
    return zip(*[inList[i:] for i in range(n)])
    
# Purpose: pads word before calling main nGram algorithm
# @param1: word to make n-gram for
# @return: Returns the n-gram as a Set object
def buildNGram(n, word):
    padded = word.center(len(word) + (n-1)*2)
    return set(*[nGram(n, padded)])
    
# Purpose: Compute ngram similarity based on the set union metric
# @param1: ngram set a
# @param2: ngram set b
# @param3: metric used as a comparison measure
# @return: returns the score as float
def compareNGram(a, b):      
    GnA = abs(len(a))
    GnB = abs(len(b))
    GnInt = abs(len(a.intersection(b)))
    return (GnA + GnB - 2*GnInt)



