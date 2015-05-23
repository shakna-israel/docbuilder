# Docbuilder

*Docbuilder is a small python script that will take another Python program, and turn it into documentation.*

Docbuilder is a tool for developing *Literate Programs* with Python.

A literate program combines both Markdown and a programming language. It is traditionally used for scientific purposes.

## Why Docbuilder?

* No need to detangle programs before running them - Python reads the Docbuilder syntax fine. If your code is written correctly, it will run.

* Generates Markdown instead of generating both Markdown and an executable file.

* The options for Literate Programming under Python is few and far between.

* Impressive compatibility. It doesn't really matter what version of Python you are running. Docbuilder will run.

# Notes:

* Docbuilder will not ask before clobbering your output file.

* Docbuilder has no dependencies.

* Docbuilder simply converts your comments and code into Markdown.

* Docbuilder builds Markdown, and is mostly compatible with whatever [Python Markdown](https://pythonhosted.org/Markdown/) can read. But just in case, check the [Issues](https://github.com/shakna-israel/docbuilder/issues).

# Dependencies:

Used to read, write and check files.


```
import os
```
Used so we can kill Docbuilder to make it behave.


```
import sys
```
Used to handle command-line arguments.


```
import argparse
```
Used for speedy opening of files


```
import fileinput
```
# Metadata:

These are used with setuptools and Pip to let people know what exactly they are installing.


```
__author__ = 'James Milne'
```

```
__version__ = '0.4'
```

```
__license__ = 'MIT'
```

```
__description__ = 'Docbuilder allows you to build Markdown documents without the need for detangling executables from literate Python programs. http://docbuilder.rtfd.org'
```
# String Manage:

*stringManage* is one of the main functions of Docbuilder.

It is in this function that each line of the Python Literate program is examined.


```
def stringManage(lineInFile):
```
verboseActive checks to see how talkative Docbuilder is expected to be.


```
    verboseActive = getFlags()[3]
```
We set up the line fed into stringManage as the unmodified *stringUnstripped* variable.


```
    stringUnstripped = lineInFile
```
We check if the line is a UNIX style *hash bang*, because we don't particularly want to see that in the documentation file.


```
    if stringUnstripped[:3] == "#!/":
```

```
        if verboseActive:
```

```
            print("Found hashbang! Ignoring.")
```
By setting *stringUnstripped* to *hashBang* it can be discarded later by another function.


```
        stringUnstripped = "hashBang"
```
If Docbuilder is talkative, it will tell the console exactly what the line it is examining looks like.


```
    if verboseActive:
```

```
        print("The current unstripped line is... " + stringUnstripped)
```
We strip the white space around the unmodified string, and name this new variable *stringStripped*.


```
    stringStripped = stringUnstripped.strip()
```
We fetch the first character of the string so we can compare it later.


```
    firstChar = stringStripped[:1]
```
If Docbuilder is talkative, it will tell us what the first character looks like.


```
    if verboseActive:
```

```
        print("The first character of the current line is..." + firstChar)
```
Then it will tell us what the whitespace stripped line looks like.


```
    if verboseActive:
```

```
        print("The current stripped line is... " + stringStripped)
```
Finally, we strip the first character from the line so we can examine it better, without having to strip the character away later.


```
    stringStripped = stringStripped[1:].strip()
```
If Docbuilder is talkative, it will tell us what that line looks like without the first character.


```
    if verboseActive:
```

```
        print("After first character stripping, the current unstripped line is..." + stringStripped)
```
Finally, we send the three variables, *stringUnstripped*, *stringStripped* and *firstChar* back to whatever function called *stringManage*.


```
    return (stringUnstripped, stringStripped, firstChar)
```
# Check Export File

This is a simple function, that gets given a file name, checks if it exists, and if so, clobbers it.


```
def checkExportFile(fileExists):
```

```
    clobberFile = getFlags()[4]
```
Check if Docbuilder should kill any file if it is pre-existing.


```
    if clobberFile:
```

```
        if os.path.isfile(fileExists):
```
If the file exists, and Docbuilder is expected to clobber, kill the file.


```
            os.remove(fileExists)
```

```
    else:
```
If the file exists, and Docbuilder is expected to not clobber, print a message and gracefully exit.


```
        if os.path.isfile(fileExists):
```

```
            print("File " + fileExists + " exists. Not clobbering.")
```

```
            sys.exit(0)     
```
# Check Export Directory

This is a naive function that gets given a directory path, checks if it exists, and if it doesn't, attempts to create it.


```
def checkExportDir(directory):
```
Check if we have a UNIX-style subdirectory being handed in.


```
    if '/' in directory:
```
Do some clever magic to walk through each of the folders given as a path, and check if the folder exists. If not, make it.


```
        previousFolder = False
```

```
        for folder in directory.split('/'):
```

```
            if not previousFolder:
```

```
                if folder != "":
```

```
                    if not os.path.exists(folder):
```

```
                        print(folder)
```

```
                        os.makedirs(folder)
```

```
                        previousFolder = folder
```

```
            else:
```

```
                if not os.path.exists(previousFolder + "/" + folder):
```

```
                    print(previousFolder + '/' + folder)
```

```
                    os.makedirs(previousFolder + "/" + folder)
```

```
                    previousFolder = previousFolder + "/" + folder
```
If we're just given a single directory, check if it exists, if not, make it.


```
    if not os.path.exists(directory):
```

```
        os.makedirs(directory)
```
# Unicode Compare Character

This is a function that only exists due to the unicode differences between Python 2.8, 3.0, and 3.3.

It checks the allowed functions and returns the correct unicode character for the code it was given.


```
def unicodeCompareChar(uniCode):
```

```
    try:
```
This is one way unicode can be handled pre Python 3.x


```
        compareChar = unichr(uniCode)
```

```
    except NameError:
```
This is one way unicode can be handled in Python 3.x, because Python 3.x uses unicode for... Everything.


```
        compareChar = chr(uniCode)
```

```
    return compareChar
```
