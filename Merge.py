import os
import ast
import Spimi
def merge():
    # List of block files
    blockFiles = ["block1.txt", "block2.txt", "block3.txt", "block4.txt", "block5.txt", "block6.txt", "block7.txt", "block8.txt","block9.txt","block10.txt",
                  "block11.txt","block12.txt","block13.txt","block14.txt","block15.txt","block16.txt","block17.txt","block18.txt","block19.txt","block20.txt",
                  "block21.txt","block22.txt","block23.txt","block24.txt","block25.txt","block26.txt","block27.txt","block28.txt","block29.txt","block30.txt",
                  "block31.txt","block32.txt","block33.txt","block34.txt","block35.txt","block36.txt","block37.txt","block38.txt","block39.txt","block40.txt",
                  "block41.txt","block42.txt","block43.txt","block44.txt"]
    index = {}
    outFile = "index.txt"

    # Read block files and merge to index file
    for file in blockFiles:
        blockFile = open("Blocks/" + file, "r")
        for line in blockFile:
            term,postingsList = line.strip().split(":")
            postingsList = ast.literal_eval(postingsList)

            if term not in index.keys():
                index[term] = postingsList
            else:
                for docid in postingsList:
                    index[term].append(docid)
    sortedIndex = Spimi.sortTerms(index)
    with open(outFile,"a+") as outFile:
        for item in sortedIndex:
            outFile.write(str(item) + ":" + str(sortedIndex[item]) + "\n")

