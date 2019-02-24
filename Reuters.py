import nltk
import string
from bs4 import BeautifulSoup

class Reuters:

	# List of Reuters filenames
	corpus = ["reut2-000.sgm", "reut2-001.sgm", "reut2-002.sgm", "reut2-003.sgm", "reut2-004.sgm", "reut2-005.sgm",
		"reut2-006.sgm", "reut2-007.sgm", "reut2-008.sgm", "reut2-009.sgm", "reut2-010.sgm", "reut2-011.sgm", "reut2-012.sgm",
		"reut2-013.sgm", "reut2-014.sgm", "reut2-015.sgm", "reut2-016.sgm", "reut2-017.sgm", "reut2-018.sgm", "reut2-019.sgm",
		"reut2-020.sgm", "reut2-021.sgm"]


	# Retreives all Reuters files and stores them in a list
	def getDocuments(self):
		documentsList = []
		for file in self.corpus:
			articleFile = open("Reuters-21578/" + file, "r")
			soup = BeautifulSoup(articleFile, 'html.parser')
			documents = soup.findAll('reuters')
			for document in documents:
				documentsList.append(document)

		# Test with just one file
		# articleFile = open("Reuters-21578/reut2-000.sgm", "r")
		# soup = BeautifulSoup(articleFile, 'html.parser')
		# documents = soup.findAll('reuters')

		return documentsList




