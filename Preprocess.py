import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
import sys
import Spimi
import Ranking
from bs4 import BeautifulSoup
from collections import OrderedDict

def preprocess(documents):
    dictionary = {}
    numOfDocs = len(documents)
    docCount = 0
    tempDocuments = []
    tokens = []
    blockCount = 0
    sumOfLengths = 0
    Lave = 0
    stopWords = set(stopwords.words('english'))

    for document in documents:
        for token in nltk.word_tokenize(document.get_text()):  # For each token in document, add to token list
            tokens.append(token)
            sumOfLengths += len(tokens)


        # if len(tempDocuments) < 500:
        #     tempDocuments.append(document)
        #     for token in nltk.word_tokenize(document.get_text()): #For each token in document, add to token list
        #         tokens.append(token)
        # else:

        # Converts all terms to lowercase
        tokens = [i.lower() for i in tokens]

        # Removes all numbers
        tokens = [i for i in tokens if not any(c.isdigit() for c in i)]

        # Removes stopwords
        tokens = [w for w in token if not w in stopWords]

        # Removes punctuation and other characters
        punctuations = '!?"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~'
        tokens = [t.translate(None, punctuations) for t in tokens]
        tokens = [t.translate(str.maketrans('','',punctuations)) for t in tokens]
        tokens = [i for i in tokens if not i in string.punctuation]

    # Get average document length for whole corpus
    # Lave = sumOfLengths / 12578
    # Ranking()



    # print(tempDocuments)
    print(document)
    for term in tokens:
        if term not in dictionary.keys():
            dictionary[term] = []
            dictionary[term].append(document['newid'])
        else:
            if document['newid'] not in dictionary[term]:
                dictionary[term].append(document['newid'])
    tokens = []


    sortedDictionary = sortTerms(dictionary)
    writeToIndex(sortedDictionary)




        # Spimi.spimi(tokens,blockCount, document['newid'])
        # tokens = []
        # tempDocuments = []
        # tempDocuments.append(document)

# Sorts the dictionary
def sortTerms(dictionary):
    sortedTerms = sorted(dictionary)
    dictionarySorted = OrderedDict()
    for item in sortedTerms:
    	dictionarySorted[item] = dictionary[item]
    return dictionarySorted

# Writes dictionary to file
def writeToIndex(sortedDictionary):
    outFile = 'index.txt'
    with open(outFile, "a+") as outFile:
        for item in sortedDictionary:
            outFile.write(str(item) + ":" + str(sortedDictionary[item]) + "\n")


