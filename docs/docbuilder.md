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
Used to handle command-line arguments.


```
import argparse
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
