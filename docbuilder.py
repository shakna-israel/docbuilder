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

## Notes:
# * Docbuilder will not ask before clobbering your output file. It may even kill the entire directory.
# * Docbuilder has no dependencies.
# * Docbuilder simply converts your comments and code into Markdown.
# * Docbuilder builds Markdown, and is mostly compatible with whatever [Python Markdown](https://pythonhosted.org/Markdown/) can read. But just in case, check the [Issues](https://github.com/shakna-israel/docbuilder/issues).

## Usage:
# Docbuilder is easy to use.
### Under Windows:
# ```python docbuilder.py PythonLiterateFile DocumentationFile DocumentationDirectory```
# e.g. ```python docbuilder.py myFile.py myFile.md docs```
### Under Linux:
# ```./docbuilder.py PythonLiterateFile DocumentationFile DocumentationDirectory```
# e.g. ```./docbuilder.py myFile.py myFile.md docs```

# * If you do not specify a DocumentationFile, Docbuilder will try and guess one for you.
# * If you don't specify a DocumentationDirectory, Docbuilder will use the ```docs``` folder.

# # Dependencies:
# ``` os ``` and ``` sys ``` are used to check if files exist, and to let you write to them.
import os
import sys

# The *FILE* variable tells Docbuilder what file it should build documentation from.
# See if the user has provided a file name to build documentation for.
try:
    # The file provided should be the first argument.
    FILE = sys.argv[1]
# If the user hasn't provided a file, just build documentation for docbuilder itself.
except IndexError:
    print("No file provided to document... Building for Docbuilder.")
    FILE = "docbuilder.py"
# The *DIRECTORY* variable tells Docbuilder where to build documentation to.
try:
    # Check if a user has specified a directory.
    DIRECTORY = sys.argv[3] + "/"
except IndexError:
    # If the user doesn't specify a directory, use docs.
    DIRECTORY = "docs/"
# The *EXPORT* variable tells Docbuilder what file it should build documentation into.
# See if the user has provided a file name to build documentation out to.
try:
    # The file to build out to should be the second argument.
    EXPORT = DIRECTORY + sys.argv[2]
# If the user hasn't, try and guess what to call the file.
except IndexError:
    print("No output file provided, guessing...")
    EXPORT = DIRECTORY + FILE + ".md"
    print(EXPORT)
# Instantiate the string variable, which is used by Docbuilder to read and write files.
stringUnstripped = "Unset"
stringStripped = "Unset"
# Check if the *EXPORT* file exists:
if os.path.isfile(EXPORT):
    # If the file exists, clobber it.
    os.remove(EXPORT)
# If the ```docs``` directory doesn't exist, make it.
if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)
# Open the file we're building documentation from in read-only mode, so we can't kill it.
inFile = open(FILE, "r")
# Open the file we're building documentation into, in write mode. Create it if it doesn't exist. (Which would happen if we clobbered it).
outFile = open(EXPORT, "w+")
# Read the file, that we're building from, into memory.
for lineRead in inFile.read().split('\n'):
    # For each line found in the file, assign it to the string variable.
    stringUnstripped = lineRead
    # Strip whitespace, because indentation can break Markdown from working.
    # We assign this to a seperate variable, so code doesn't have it's identation stolen.
    stringStripped = stringUnstripped.strip()
    # Assign the variable *char* to the first character in string. So we can tell if it's a comment, and should be seen as valid Markdown, or if it's not, should be fenced in a code block.
    firstChar = stringStripped[:1]
    # Test to make unicode literals work on Python 2.x-3.x (Especially 3.0, 3.1, 3.2)
    try:
        compareChar = unichr(35)
    except NameError:
        compareChar = chr(35)
    # Check if the first character is a *#* to see if it is a comment, and should be markdown.
    if firstChar == compareChar:
        # Strip the whitespace. So if there is an ident between comment beginning, and Markdown, it isn't a problem.
        stringStripped = stringUnstripped.strip()
        # Remove the first letter, and strip the whitespace.
        stringStripped = stringStripped[1:].strip()
        # Push every string onto it's own line.
        outFile.write("\n")
        outFile.write(stringStripped)
        outFile.write("\n")
    # If the first character isn't a *#*, turn it into a codeblock.
    else:
        # Make sure we aren't just looking at a blank line.
        if string != "":
            # Push it onto it's own line.
            outFile.write("\n")
            # Open the codeblock fence.
            outFile.write("```")
            # Due to Markdown, make it a block by inserting EOLs before and after the string.
            outFile.write("\n")
            # Insert the code
            outFile.write(stringUnstripped)
            outFile.write("\n")
            # Close the codeblock fence.
            outFile.write("```")
            # Make sure there's a gap, so Markdown plays nice.
            outFile.write("\n")

# Close out the file we're reading, to make sure we aren't leaving it locked.
inFile.close()
# Close out the file we wrote, to make sure we aren't leaving it locked.
outFile.close()
