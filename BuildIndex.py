import Reuters
import Preprocess
import Preprocess2
import Spimi
import Merge
import sys

# Retrieves Reuters documents
print("Retrieving documents..")
r1 = Reuters.Reuters()
documents = r1.getDocuments()

# Tokenizes each document
print("Tokenizing..")
Preprocess.preprocess(documents)

#Test with smaller set of documents
# print("Tokenizing2...")
# Preprocess2.preprocess2(documents)

# Calls merge method
# print("Merging blocks..")
# Merge.merge()




