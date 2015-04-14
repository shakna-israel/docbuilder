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

# # Global Variables:
# *FILE* is used to tell Docbuilder what file to build documentation for.
global FILE
# *DIRECTORY* is used to tell Docbuilder where to build documentation to.
global DIRECTORY
# *EXPORT* is used to tell DOcbuilder what file to build documentation into.
global EXPORT
# *verboseActive* is used to tell Docbuilder to say more on the commandline. A lot more.
global verboseActive
# *stringUnstripped* is used to tell Docbuilder what the current line of the file being processed looks like.
global stringUnstripped
# *stringStripped* tells Docbuilder what the current line of the file being process looks like without whitespace.
global stringStripped
# *firstChar* tell Docbuilder what the first character of the current line of the file being processed looks like.
global firstChar
# *compareChar* is a unicode symbol for the hash symbol, to prevent Python breaking Docbuilder's code.
global compareChar
# *outFile* tells Docbuilder what memory object is the file it is writing to.
global outFile

def fileReadFrom(input):
    global FILE
    checkExportFile(input)
    FILE = input

def directoryWriteTo(dir):
    global DIRECTORY
    checkExportDir(dir)
    DIRECTORY = dir + "/"

def fileWriteTo(input):
    global EXPORT
    try:
        EXPORT = DIRECTORY + "/" + input
    except IndexError:
        EXPORT = DIRECTORY + FILE + ".md"
        if verboseActive:
            print("No output file provided, guessing... " + EXPORT)

def stringManage(line):
    global stringUnstripped
    global stringStripped
    global firstChar
    stringUnstripped = line
    if verboseActive:
        print("The current unstripped line is... " + stringUnstripped)
    stringStripped = stringUnstripped.strip()
    if verboseActive:
        print("The current stripped line is... " + stringStripped)
    firstChar = stringStripped[:1]
    if verboseActive:
        print("The first character of the current line is..." + firstChar)

def checkExportFile(input):
    if os.path.isfile(input):
        os.remove(input)

def checkExportDir(input):
    if not os.path.exists(input):
        os.makedirs(input)

def unicodeCompareChar(input):
    global compareChar
    try:
        compareChar = unichr(input)
    except NameError:
        compareChar = chr(input)

def markdownWrite(input):
    global outFile
    outFile.write("\n")
    outFile.write(input)
    outFile.write("\n")

def codeblockWrite(input):
    global outFile
    outFile.write("\n```\n")
    outFile.write(input)
    outFile.write("\n```\n")

def readFile(input, output):
    global outFile
    inFile = open(input, "r")
    outFile = open(output, "w+")
    for lineRead in inFile.read().split("\n"):
        stringManage(input)
        unicodeCompareChar(35)
        if firstChar == compareChar:
            markdownWrite(stringStripped)
        else:
            if stringUnstripped != "":
                codeblockWrite(stringUnstripped)
    inFile.close()
    outFile.close()

def main():
    global verboseActive
    global FILE
    global DIRECTORY
    verboseActive = True
    try:
        readFile = fileReadFrom(sys.argv[1])
    except IndexError:
        if verboseActive:
            print("No file specified. Building documentation for Docbuilder")
        readFile = fileReadFrom("docbuilder.py")
    try:
        directoryWriteTo(sys.argv[3])
    except:
        if verboseActive:
            print("No output directory specified. Using 'docs' directory.")
        directoryWriteTo("docs")
    try:
        fileWriteTo(sys.argv[2])
    except IndexError:
        fileWriteTo(DIRECTORY + FILE + ".md")
        if verboseActive:
            print("No output file specified. Guessing..." + DIRECTORY + FILE + ".md")
    readFile(fileReadFrom("docbuilder.py"), fileWriteTo("docs"))

if __name__ =='__main__':main()
