# Embedding Docbuilder

Docbuilder is fairly simple to embed, as of v0.6, as you can now simply create a Docbuilder object.

This example will show you how to generate a Markdown file,

using a Docbuilder object, but you could equally use a StringIO object to store the output.

First, we import docbuilder


```
import docbuilder
```
Then, we create a Docbuilder object:


```
builder = docbuilder.Docbuilder()
```
Then, we set the flags we want, by generating a dictionary.


```
flagsDict = {'inFile': "embeddedDocbuilder.pylit", 'outDir': "../docs", 'outFile': "embeddedDocbuilder"}
```
We tell our object where to use the flags


```
builder.setFlags(flagsDict)
```
Check if the output file exists


```
builder.checkExportFile(flagsDict['outFile'])
```
Read the input file


```
builder.readFile(flagsDict['inFile'])
```
