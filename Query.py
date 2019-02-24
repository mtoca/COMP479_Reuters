import ast

index = {}
terms = []
listOfPostingsList = []
operator = ""

# Displays result set based on operators (AND, OR or " ")
def displayResults(operator):
    results = []
    if operator == "or" or operator == " ":
        results = set.union(*map(set, listOfPostingsList))
        results = [int(result) for result in results]
        results = sorted(results)
    else:
        if operator == "and":
            results = set.intersection(*map(set, listOfPostingsList))
            results = [int(result) for result in results]
            results = sorted(results)
    print(results)

# Reads index from disk to memory
print("Reading index into memory..")
indexFile = open("index.txt", "r")
for line in indexFile:
    term, postingsList = line.strip().split(":")
    postingsList = ast.literal_eval(postingsList)
    index[term] = postingsList

# Parses query input and splits terms accordingly
while True:
    print("Enter your query: ")
    query = input()
    query = query.lower()
    if 'or' in query:
        operator = "or"
        terms = query.split(' or ')
        for term in terms:
            if term in index.keys():
                listOfPostingsList.append(index[term])
        print("Results: ")
        displayResults(operator)
    elif 'and' in query:
            operator = "and"
            terms = query.split(' and ')
            for term in terms:
                if term in index.keys():
                    listOfPostingsList.append(index[term])
            # del listOfPostingsList[0]
            print("Results: ")
            displayResults(operator)
    else:
        operator = " "
        terms = query.split(" ")
        for term in terms:
            if term in index.keys():
                listOfPostingsList.append(index[term])
        print("Results: ")
        displayResults(operator)
    listOfPostingsList = []

