import nltk
import string
import sys
from bs4 import BeautifulSoup
from collections import OrderedDict

# Spimi Algorithm - Writes to dictionary for each block
def spimi(token_stream, blockCount, docID):
    dictionary = {}

    for term in token_stream:
        if term not in dictionary.keys():
            dictionary[term] = []
            dictionary[term].append(docID)
        else:
            if docID not in dictionary[term]:
                dictionary[term].append(docID)

    sortedDictionary = sortTerms(dictionary)
    # blockFile = outBlockFile(sortedDictionary, blockCount)
    writeToIndex(sortedDictionary)
    dictionary = {}


# Sorts the dictionary
def sortTerms(dictionary):
    sortedTerms = sorted(dictionary)
    dictionarySorted = OrderedDict()
    for item in sortedTerms:
    	dictionarySorted[item] = dictionary[item]
    return dictionarySorted

# Prints each block to file
def outBlockFile(sortedTerms, fileCount):
    outFile = 'Blocks/block' + str(fileCount) + '.txt'
    with open(outFile, "a+") as outFile:
        for item in sortedTerms:
            outFile.write(str(item) + ":" + str(sortedTerms[item]) + "\n")
    return outFile

# Writes dictionary to file
def writeToIndex(sortedDictionary):
    outFile = 'index.txt'
    with open(outFile, "a+") as outFile:
        for item in sortedDictionary:
            outFile.write(str(item) + ":" + str(sortedDictionary[item]) + "\n")


