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

# # String Manage:
# *stringManage* is one of the main functions of Docbuilder.
# It is in this function that each line of the Python Literate program is examined.
def stringManage(lineInFile):
    # verboseActive checks to see how talkative Docbuilder is expected to be.
    global verboseActive
    # We set up the line fed into stringManage as the unmodified *stringUnstripped* variable.
    stringUnstripped = lineInFile
    # We check if the line is a UNIX style *hash bang*, because we don't particularly want to see that in the documentation file.
    if stringUnstripped[:3] == "#!/":
        if verboseActive:
            print("Found hashbang! Ignoring.")
        # By setting *stringUnstripped* to *hashBang* it can be discarded later by another function.
        stringUnstripped = "hashBang"
    # If Docbuilder is talkative, it will tell the console exactly what theline it is examining looks like.
    if verboseActive:
        print("The current unstripped line is... " + stringUnstripped)
    # We strip the white space around the unmodified string, and name this new variable *stringStripped*.
    stringStripped = stringUnstripped.strip()
    # We fetch the first character of the string so we can compare it later.
    firstChar = stringStripped[:1]
    # If Docbuilder is talkative, it will tell us what the first character looks like.
    if verboseActive:
        print("The first character of the current line is..." + firstChar)
    # Then it will tell us what the whitespace stripped line looks like.
    if verboseActive:
        print("The current stripped line is... " + stringStripped)
    # Finally, we strip the first character from the line so we can examine it better, without having to strip the character away later.
    stringStripped = stringStripped[1:].strip()
    # If Docbuilder is talkative, it will tell us what that line looks like without the first character.
    if verboseActive:
        print("After first character stripping, the current unstripped line is..." + stringStripped)
    # Finally, we send the three variables, *stringUnstripped*, *stringStripped* and *firstChar* back to whatever function called *stringManage*.
    return (stringUnstripped, stringStripped, firstChar)

# # Check Export File
# This is a simple function, that gets given a file name, checks if it exists, and if so, clobbers it.
def checkExportFile(fileExists):
    if os.path.isfile(fileExists):
        os.remove(fileExists)

# # Check Export Directory
# This is a simplefunction that gets given a directory path, checks if it exists, and if it doesn't, attempts to create it.        
def checkExportDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# # Unicode Compare Character
# This is a function that only exists due to the unicode differences between Python 2.8, 3.0, and 3.3.
# It checks the allowed functions are returns the correct unicode character for the code it was given.
def unicodeCompareChar(uniCode):
    try:
        compareChar = unichr(uniCode)
    except NameError:
        compareChar = chr(uniCode)
    return compareChar

# # Markdown Write
# This is a simple function, that is given both a line of Markdown to write, and a file to append to.
# It takes that file, and attempts to append it, ensuring aline break underneath each line for compatibility's sake.
def markdownWrite(stringLine, fileToWrite):
    outFile = open(fileToWrite, "a")
    outFile.write(stringLine + "\n\n")
    outFile.close()

# # Codeblock Write
# This is a function that, when given a line and file to append to, attempts to turn that line into a Markdown codeblock.
def codeblockWrite(stringLine, fileToWrite):
    # Firstly, it checks if the line is simply *hashBang*, a line created by *stringManage*, and it is, refuses to write it.
    if stringLine != "hashBang":
        # It then proceeds to append to the given file, inside a Markdown codeblock.
        outFile = open(fileToWrite, "a")
        outFile.write("\n```\n" + stringLine + "\n```\n")
        outFile.close()

# # Initiate File Out
# This is a simple function that attempts to create a file in a cross-platform friendly way, based on a file location itis given.
def initFileOut(outFile):
    initFile = open(outFile, "w+")
    initFile.close()

# # Read File
# *readFile* is function that attempts to read a Python Literate Program, and send each line it reads away to be parsed.
def readFile(inputFile):
    # Firstly, it checks to see what file the documentation is supposed to be getting written to.
    outFile = getFlags()[1]
    # It then opens the file given the path it has received, in read-only mode.
    inFile = open(inputFile, "r")
    # It asks (nicely) that the file being written to be created.
    initFileOut(outFile)
    # It then reads the file it was given, line by line.
    for lineRead in inFile.read().split("\n"):
        # For each line it reads, it asks *stringManage* to deal with.
        stringUnstripped = stringManage(lineRead)[0]
        stringStripped = stringManage(lineRead)[1]
        firstChar = stringManage(lineRead)[2]
        # It initiates the first-line comparator (#) so it can compare.
        compareChar = unicodeCompareChar(35)
        # If the first line is a hash, and not just *hashBang*, it asks *markdownWrite* to write some Markdown.
        if firstChar == compareChar:
            if stringUnstripped != "hashBang":
                markdownWrite(stringStripped, outFile)
        else:
            # Otherwise, if the line isn't an empty line, it asks *codeBlockWrite* to write a Markdown codeblock.
            if stringUnstripped != "":
                codeblockWrite(stringUnstripped, outFile)
    inFile.close()

# # Get Flags
# *getFlags* is the function that attempts to see what the user is asking of Docbuilder.
def getFlags():
    # *dirSet* is set to false, so that a flag can be read correctly later.
    dirSet = False
    # *outDir* and *outName* are set to empty so that flags can be read nicely later.
    outDir = ""
    outName = ""
    # In this for loop, *getFlags* attempts to find any flags given to Docbuilder.
    for flag in sys.argv:
        # Here, these two if statements colloborate to find what directory the user is trying to write to.
        if dirSet:
            outDir = flag + "/"
        if flag == "-d":
            dirSet = True
    # Here, *getFlags* tries to find what explicit file the user is trying to build documentation for, in a cross-platform way.
    try:
        if os.name == "nt":
            for splitRead in sys.argv[1].split(r'"\"'):
                outName = splitRead
        else:
            for splitRead in sys.argv[1].split("/"):
                outName = splitRead
        inFile = sys.argv[1]
    # Otherwise, docbuilder will assume you are just trying to write it's own documentation.
    except IndexError:
        inFile = "docbuilder.py"
        outName = "docbuilder.py"
    # This littlestatement is deprecated, but represents the old way Docbuilder determined directories.
    if outDir == "":
        try:
            outDir = sys.argv[3] + "/"
            print("This usage is deprecated and will be removed in 1.0... Use the -d flag.")
        except IndexError:
            outDir = "docs/"
    # *getFlags* nicely tries to get the documentation directory built.
    checkExportDir(outDir)
    # Here, *getFlags* tries to work out what the filename and path of the document it is building should be.
    try:
        outFile = outDir + sys.argv[2]
    except IndexError:
        # If the user never gave one just try and guess what it is.
        outFile = outDir + outName + ".md"
    # *getFlags* then nicely asks that whatever file with the same path that may exist, be removed.
    checkExportFile(outFile)
    
    # *getFlags* then returns the paths for file given by the user, the file Docbuilder is creating, and the directory being created to whatever function called it.
    return (inFile, outFile, outDir)

# # Main
# This is the main function that sets Docbuilder running.
def main():
    # Currently, this is where Docbuilder can be told to be talkative, or not.
    global verboseActive
    verboseActive = False
    # The *main* function asks *getFlags* what file the user is generating documentation for.
    inFile = getFlags()[0]
    # It then tells *readFile* what file it is building documentation for.
    readFile(inFile)
    

# # If Name
# This is a simple function that tells Python what the main function is.    
if __name__ == '__main__':
    main()
