#!/usr/bin/env python

## Docbuilder
# * Docbuilder is a small python script that will take another Python program, and turn it into documentation.
# * Docbuilder is used to generate technical documentation. It isn't reccomended at this stage for User Documentation.
# * It makes use of MkDocs as it's documentation engine, though it doesn't require it to be installed.

## Notes:
# * Docbuilder will *clobber* your docs/*FILE*. It just will... Unless you change the *EXPORT* variable to something else... Then it will clobber whatever that is.
# * Docbuilder won't generate a *mkdocs.yml* file for you. You'll need to either make one, or just use ``` mkdocs new . ``` in your current folder. [Coming in V1].
# * Docbuilder has no dependencies, except those that come with Python 2.7. (Previous versions of Python probably need some modifications to work. Python 3.x also will need some modification.)
# * Docbuilder simply converts your comments and code into Markdown, and mkdocs can serve or build that for you.
# * Docbuilder builds Markdown, and is mostly compatible with whatever [Python Markdown](https://pythonhosted.org/Markdown/) can read. But just in case, check the [Issues](https://github.com/shakna-israel/docbuilder/issues).

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
except:
    print("No file provided to document... Building for Docbuilder.")
    FILE = "docbuilder.py"
# The *DIRECTORY* variable tells Docbuilder where to build documentation to.
try:
    # Check if a user has specified a directory.
    DIRECTORY = sys.argv[3] + "/"
except:
    # If the user doesn't specify a directory, use docs.
    DIRECTORY = "docs/"
# The *EXPORT* variable tells Docbuilder what file it should build documentation into.
# See if the user has provided a file name to build documentation out to.
try:
    # The file to build out to should be the second argument.
    EXPORT = DIRECTORY + sys.argv[2]
# If the user hasn't, try and guess what to call the file.
except:
    print("No output file provided, guessing...")
    EXPORT = DIRECTORY + FILE + ".md"
    print(EXPORT)
# Instantiate the string variable, which is used by Docbuilder to read and write files.
string = "Unset"
# Check if the *EXPORT* file exists:
if os.path.isfile(EXPORT):
    # If the file exists, clobber it.
    os.remove(EXPORT)
# If the ```docs``` directory doesn't exist, make it.
if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)
# Open the file we're building documentation from in read-only mode, so we can't kill it.
file = open(FILE, "r")
# Open the file we're building documentation into, in write mode. Create it if it doesn't exist. (Which would happen if we clobbered it).
outfile = open(EXPORT, "w+")
# Read the file, that we're building from, into memory.
for line in file.read().split('\n'):
    # For each line found in the file, assign it to the string variable.
    string = line
    # Strip whitespace, because indentation can break Markdown from working. However, as seen in [#2](https://github.com/shakna-israel/write-good-py/issues/2) and [#3](https://github.com/shakna-israel/write-good-py/issues/3)
    string = string.strip()
    # Assign the variable *char* to the first character in string. So we can tell if it's a comment, and should be seen as valid Markdown, or if it's not, should be fenced in a code block.
    char = string[:1]
    # Hack to make Docbuilder pass on Python 2.x-3.x (Especially 3.0, 3.1, 3.2)
    try:
        compare_char = unichr(35)
    except:
        compare_char = chr(35)
    # Check if the first character is a *#* to see if it is a comment, and should be markdown.
    if char == compare_char:
        # Strip the whitespace. So if there is an ident between comment beginning, and Markdown, it isn't a problem.
        string = string.strip()
        # Remove the first letter, and strip the whitespace.
        string = string[1:].strip()
        # Push every string onto it's own line.
        outfile.write("\n")
        outfile.write(string)
        outfile.write("\n")
    # If the first character isn't a *#*, turn it into a codeblock.
    else:
        # Make sure we aren't just looking at a blank line.
        if string != "":
            # Push it onto it's own line.
            outfile.write("\n")
            # Open the codeblock fence.
            outfile.write("```")
            # Due to MKDocs, make it a block by inserting EOLs before and after the string.
            outfile.write("\n")
            # Insert the code
            outfile.write(string)
            outfile.write("\n")
            # Close the codeblock fence.
            outfile.write("```")
            # Make sure there's a gap, so Markdown plays nice.
            outfile.write("\n")

# Close out the file we're reading, to make sure we aren't leaving it locked.
file.close()
# Close out the file we wrote, to make sure we aren't leaving it locked.
outfile.close()
