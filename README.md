# COMP479_Reuters
Probabilistic Search Engine

The query system uses the BM25 algorithm to return and rank documents based on their scores.

The Ranking.py file is the main component. When it is executed, the program will start by retrieving all documents of the corpus, read the index.txt file from disk to memory and then prompt the user to enter a query. The query is then processed and each of the terms' posting will be added to a docID postings list.

The scores per document are then added to a list and sorted in descending order. The top 10 results are then displayed.
