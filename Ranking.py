import ast
import Reuters
import nltk
import math
import operator

score = {}
index = {}
terms = []
listOfPostingsList = []
docIDList = []
sumOfLengths = 0

N = 21578  # Number of documents in corpus
k = 0.5
b = 0.5

# Retrieve documents
print("Retrieving documents..")
r1 = Reuters.Reuters()
documents = r1.getDocuments()

# Reads index from disk to memory
print("Reading index into memory..")
indexFile = open("index.txt", "r")
for line in indexFile:
    term, postingsList = line.strip().split(":")
    postingsList = ast.literal_eval(postingsList)
    index[term] = postingsList

# Parses query input, splits terms and adds the postings list to the docIDList
while True:
    print("Enter your query: ")
    query = input()
    query = query.lower()
    terms = query.split()
    for term in terms:
        if term in index.keys():
            for item in index[term]:
                if item not in docIDList:
                    docIDList.append(item)

    # Get average document length for whole corpus
    for document in documents:
        sumOfLengths += (len(nltk.word_tokenize(document.get_text())))
        Lave = sumOfLengths/21578

    # Getting length of each document (# of tokens in document)
    for docID in docIDList:
        Ld = 0
        tf_idf_sum = 0
        for document in documents:
            if document['newid'] == docID:
                Ld = len(nltk.word_tokenize(document.get_text()))

        # For each term in query, get term frequency and document frequency
        for term in terms:
            tf = 0
            df = 0

            # Get term frequency (tf)
            for document in documents:
                if document['newid'] == docID:
                    for token in nltk.word_tokenize(document.get_text().lower()):
                        if token==term:
                            tf += 1
            # Get document frequency (df)
            if term in index:
                df = len(index[term])

            # Plug everything in BM25 formula
            idf = math.log10(N/df)
            tf_norm = ((k + 1) * tf) / ((k * ((1 - b) + (b * (Ld / Lave)))) + tf)
            tf_idf = idf * tf_norm
            tf_idf_sum += tf_idf

        # Add scores to list
        score[docID] = tf_idf_sum

    # Sort scores in descending order
    top_results = sorted(score.items(), key=operator.itemgetter(1), reverse=True)

    # Print top 10 results
    print(top_results[:10])

