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
# Used so we can kill Docbuilder to make it behave.
import sys
# Used to handle command-line arguments.
import argparse
# Used to make docbuilder a little speedier
import fileinput

# # Metadata:
# These are used with setuptools and Pip to let people know what exactly they are installing.

__author__ = 'James Milne'
__version__ = '0.4'
__license__ = 'MIT'
__description__ = 'Docbuilder allows you to build Markdown documents without the need for detangling executables from literate Python programs. http://docbuilder.rtfd.org'

# # String Manage:
# *stringManage* is one of the main functions of Docbuilder.
# It is in this function that each line of the Python Literate program is examined.
def stringManage(lineInFile):
    # verboseActive checks to see how talkative Docbuilder is expected to be.
    verboseActive = getFlags()[3]
    # We set up the line fed into stringManage as the unmodified *stringUnstripped* variable.
    stringUnstripped = lineInFile
    # We check if the line is a UNIX style *hash bang*, because we don't particularly want to see that in the documentation file.
    if stringUnstripped[:3] == "#!/":
        if verboseActive:
            print("Found hashbang! Ignoring.")
        # By setting *stringUnstripped* to *hashBang* it can be discarded later by another function.
        stringUnstripped = "hashBang"
    # If Docbuilder is talkative, it will tell the console exactly what the line it is examining looks like.
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
    clobberFile = getFlags()[4]
    # Check if Docbuilder should kill any file if it is pre-existing.
    if clobberFile:
        if os.path.isfile(fileExists):
            # If the file exists, and Docbuilder is expected to clobber, kill the file.
            os.remove(fileExists)
    else:
        # If the file exists, and Docbuilder is expected to not clobber, print a message and gracefully exit.
        if os.path.isfile(fileExists):
            print("File " + fileExists + " exists. Not clobbering.")
            sys.exit(0)     

# # Check Export Directory
# This is a naive function that gets given a directory path, checks if it exists, and if it doesn't, attempts to create it.        
def checkExportDir(directory):
    # Check if we have a UNIX-style subdirectory being handed in.
    if '/' in directory:
        # Do some clever magic to walk through each of the folders given as a path, and check if the folder exists. If not, make it.
        previousFolder = False
        for folder in directory.split('/'):
            if not previousFolder:
                if folder != "":
                    if not os.path.exists(folder):
                        print(folder)
                        os.makedirs(folder)
                        previousFolder = folder
            else:
                if not os.path.exists(previousFolder + "/" + folder):
                    print(previousFolder + '/' + folder)
                    os.makedirs(previousFolder + "/" + folder)
                    previousFolder = previousFolder + "/" + folder
    # If we're just given a single directory, check if it exists, if not, make it.
    if not os.path.exists(directory):
        os.makedirs(directory)

# # Unicode Compare Character
# This is a function that only exists due to the unicode differences between Python 2.8, 3.0, and 3.3.
# It checks the allowed functions and returns the correct unicode character for the code it was given.
def unicodeCompareChar(uniCode):
    try:
        # This is one way unicode can be handled pre Python 3.x
        compareChar = unichr(uniCode)
    except NameError:
        # This is one way unicode can be handled in Python 3.x, because Python 3.x uses unicode for... Everything.
        compareChar = chr(uniCode)
    return compareChar

# # Markdown Write
# This is a simple function, that is given both a line of Markdown to write, and a file to append to.
# It takes that file, and attempts to append it, ensuring aline break underneath each line for compatibility's sake.
def markdownWrite(stringLine, fileToWrite):
    verboseActive = getFlags()[3]
    if verboseActive:
        print("Attempting to open " + fileToWrite + " file to append...")
    # Open the file in append mode.
    outFile = open(fileToWrite, "a")
    # Write the line we're given, and append a blank line underneath.
    outFile.write(stringLine + "\n\n")
    if verboseActive:
        print("Closing " + fileToWrite + " file.")
    # Close out the file, so we aren't doing anything blocking.
    # This open/close procedure for every line should help with some race conditions, if they happen.
    outFile.close()

# # Codeblock Write
# This is a function that, when given a line and file to append to, attempts to turn that line into a Markdown codeblock.
def codeblockWrite(stringLine, fileToWrite):
    verboseActive = getFlags()[3]
    # Firstly, it checks if the line is simply *hashBang*, a line created by *stringManage*, and it is, refuses to write it.
    if stringLine != "hashBang":
        # It then proceeds to append to the given file, inside a Markdown codeblock.
        if verboseActive:
            print("Attempting to open " + fileToWrite + " file to append...")
        # Open the file in append file.
        outFile = open(fileToWrite, "a")
        # Append the line we're given inside a code block, with a newline before and after.
        outFile.write("\n```\n" + stringLine + "\n```\n")
        if verboseActive:
            print("Closing " + fileToWrite + " file.")
        # Close out the file.
        # This open/close procedure for every line should help with some race conditions, if they happen.
        outFile.close()

# # Initiate File Out
# This is a simple function that attempts to create a file in a cross-platform friendly way, based on a file location itis given.
def initFileOut(outFile):
    verboseActive = getFlags()[3]
    if verboseActive:
        print("Attempting to create file... " + outFile + ".")
    # Try and create the file by opening it. If it doesn't exist, Python should create it.
    initFile = open(outFile, "w+")
    if verboseActive:
        print("Closing new file... " + outFile + ".")
    # Close out the file, because all we're doing right now is creating it.
    # This function could be problematic with some race conditions, if the file is edited before closing out, we could get hit by some memory errors.
    initFile.close()

# # Read File
# *readFile* is function that attempts to read a Python Literate Program, and send each line it reads away to be parsed.
def readFile(inputFile):
    # Firstly, it checks to see what file the documentation is supposed to be getting written to.
    outFile = getFlags()[1]
    # It then opens the file given the path it has received as a stream.
    inFile = fileinput.input(inputFile)
    # It asks (nicely) that the file being written to be created.
    initFileOut(outFile)
    # Check if we want Markdown Indented or not
    markdownIndent = getFlags()[5]
    # It then reads the file it was given, line by line.
    for lineRead in inFile:
        # Ignore blank lines
        if lineRead == "\n":
            continue
        # For each line it reads, it asks *stringManage* to deal with.
        stringUnstripped = stringManage(lineRead)[0]
        stringStripped = stringManage(lineRead)[1]
        firstChar = stringManage(lineRead)[2]
        # It initiates the first-line comparator (#) so it can compare.
        compareChar = unicodeCompareChar(35)
        # If the first line is a hash, and not just *hashBang*, it asks *markdownWrite* to write some Markdown.
        if firstChar == compareChar:
            if stringUnstripped != "hashBang":
                # If the user wants indented Markdown, run things a little differently.
                if markdownIndent:
                    # Strip only the first two characters. These should be a hash, ```#```, and a space, ``` ```.
                    indentedString = stringUnstripped[2:]
                    markdownWrite(indentedString, outFile)
                # If the user doesn't want indented Markdown, just ask the *markdownWrite* function to do its job.
                else:
                    markdownWrite(stringStripped, outFile)
        else:
            # Otherwise, if the line isn't an empty line, it asks *codeBlockWrite* to write a Markdown codeblock.
            # The strip() statement is just to ensure there isn't any invisible indentation that might muck us around.
            if stringUnstripped.strip() != "":
                codeblockWrite(stringUnstripped, outFile)
    inFile.close()

# # Get Flags
# *getFlags* is the function that attempts to see what the user is asking of Docbuilder.
# It's also where we define the Public API.
# NOTE: All command-line arguments are *optional*, Docbuilder will build it's own documentation if given no arguments.
def getFlags():
    # Initialise our parser for arguments.
    parser = argparse.ArgumentParser()
    # Create the parsing for the input file. (The file to build documentation from).
    parser.add_argument("-i", "--input", help="The input file. Normally, a *.pylit file.")
    # Create the parsing for the output file. (The file to build documentation for).
    parser.add_argument("-o", "--output", help="The output file name, without file extension.")
    # Create the parsing for verbose arguments.
    parser.add_argument("-v", "--verbose", help="Print more information to the console", action="store_true")
    # Create the parsing for the output directory.
    parser.add_argument("-d", "--directory", help="Set the output directory.")
    # Create the parsing for Markdown Indentation.
    parser.add_argument("--indent", help="Indent Markdown", action="store_true")
    # Create the parsing for file clobbering politeness.
    parser.add_argument("-q", "--quiet", help="Clobber existing files without asking.", action="store_true")
    # Simplify parsing the arguments.
    cliArgs = parser.parse_args()
    # Work out the filepath of the file Docbuilder is building documentation for.
    if cliArgs.input:
        inFile = cliArgs.input
    # If the user didn't specify a file, assume they're build Docbuilder's own documentation.
    else:
        inFile = "docbuilder.py"
    # Set whether verbose is turned on or not:
    if cliArgs.verbose:
        verboseActive = True
    # If the user didn't ask for verbose, set Docbuilder to not be verbose.
    else:
        verboseActive = False
    # Set what directory Docbuilder will build to:
    if cliArgs.directory:
        outDir = cliArgs.directory + "/"
        # If the output directory doesn't exist, ask Docbuilder to create it.
        checkExportDir(outDir)
    # If the user didn't specify a directory, assume they want the *docs* directory.
    else:
        outDir = "docs" + "/"
    # Set the output file path.
    if cliArgs.output:
        outFile = outDir + cliArgs.output + ".md"
    else:
        # If the user specified an input file, try and magic up a name.
        if cliArgs.input:
            outFile = outDir + cliArgs.input + ".md"
        # If the user didn't specify an input file either, build for Docbuilder.
        else:
            outFile = outDir + "docbuilder.md"
    # Set Docbuilder's politeness when clobbering files.
    if cliArgs.quiet:
        clobberFile = True
    else:
        clobberFile = False
    # Check if the user wants Markdown indented.
    if cliArgs.indent:
        markdownIndent = True
    else:
        markdownIndent = False
    # Return the found values.
    return (inFile, outFile, outDir, verboseActive, clobberFile, markdownIndent)

# # Main
# This is the main function that sets Docbuilder running.
def main():
    # The *main* function asks *getFlags* what file the user is generating documentation for.
    inFile = getFlags()[0]
    # The *main* function asks *getFlags* what file the user is generating documentation to.
    outFile = getFlags()[1]
    # The main function checks if the output file pre-exists.
    checkExportFile(outFile)
    # It then tells *readFile* what file it is building documentation for.
    readFile(inFile)

# This is a simple function that tells Python what the main function is.    
if __name__ == '__main__':
    main()
