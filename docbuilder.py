#!/usr/bin/env python

# # Docbuilder
# *Docbuilder is a small python script that will take another Python program, and turn it into documentation.*
# Docbuilder is a tool for developing *Literate Programs* with Python.
# A literate program combines both Markdown and a programming language. It is traditionally used for scientific purposes.
# ## Why Docbuilder?
# * No need to detangle programs before running them - Python reads the Docbuilder syntax fine. If your code is written correctly, it will run.
# * Generates Markdown instead of generating both Markdown and an executable file.
# * The options for Literate Programming under Python is few and far between.
# * Impressive compatibility. It doesn't really matter what version of Python you are running. Docbuilder will run.

# # Notes:
# * Docbuilder will not ask before clobbering your output file.
# * Docbuilder has no dependencies.
# * Docbuilder simply converts your comments and code into Markdown.
# * Docbuilder builds Markdown, and is mostly compatible with whatever [Python Markdown](https://pythonhosted.org/Markdown/) can read. But just in case, check the [Issues](https://github.com/shakna-israel/docbuilder/issues).

# # Dependencies:
# Used to read, write and check files.
import os
import sys

def stringManage(lineInFile):
    global verboseActive
    stringUnstripped = lineInFile
    if verboseActive:
        print("The current unstripped line is... " + stringUnstripped)
    stringStripped = stringUnstripped.strip()
    firstChar = stringStripped[:1]
    if verboseActive:
        print("The first character of the current line is..." + firstChar)
    if verboseActive:
        print("The current stripped line is... " + stringStripped)
    stringStripped = stringStripped[1:].strip()
    if verboseActive:
        print("After first character stripping, the current unstripped line is..." + stringStripped)
    return (stringUnstripped, stringStripped, firstChar)

def checkExportFile(fileExists):
    if os.path.isfile(fileExists):
        os.remove(fileExists)

def checkExportDir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def unicodeCompareChar(uniCode):
    try:
        compareChar = unichr(uniCode)
    except NameError:
        compareChar = chr(uniCode)
    return compareChar

def markdownWrite(stringLine, fileToWrite):
    outFile = open(fileToWrite, "a")
    outFile.write("\n")
    outFile.write(stringLine)
    outFile.write("\n")
    outFile.close()

def codeblockWrite(stringLine, fileToWrite):
    outFile = open(fileToWrite, "a")
    outFile.write("\n```\n")
    outFile.write(stringLine)
    outFile.write("\n```\n")
    outFile.close()

def initFileOut(outFile):
    initFile = open(outFile, "w+")
    initFile.close()

def readFile(inputFile, outputFile):
    outFile = getFlags()[1]
    inFile = open(inputFile, "r")
    initFileOut(outFile)
    for lineRead in inFile.read().split("\n"):
        stringUnstripped = stringManage(lineRead)[0]
        stringStripped = stringManage(lineRead)[1]
        firstChar = stringManage(lineRead)[2]
        compareChar = unicodeCompareChar(35)
        if firstChar == compareChar:
            markdownWrite(stringStripped, outFile)
        else:
            if stringUnstripped != "":
                codeblockWrite(stringUnstripped, outFile)
    inFile.close()

def getFlags():
    try:
        inFile = sys.argv[1]
    except IndexError:
        inFile = "docbuilder.py"
    try:
        outDir = sys.argv[3] + "/"
    except IndexError:
        outDir = "docs/"
    checkExportDir(outDir)
    try:
        outFile = outDir + sys.argv[2]
    except IndexError:
        outFile = outDir + inFile + ".md"
    checkExportFile(outFile)
    return (inFile, outFile, outDir)

def main():
    global verboseActive
    verboseActive = False
    inFile = getFlags()[0]
    outFile = getFlags()[1]
    readFile(inFile, outFile)
    
if __name__ =='__main__':main()
