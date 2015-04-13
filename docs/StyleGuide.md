Style Guide
============

The Docbuilder syntax attempts to replicate both Markdown and Python closely, however there are a few minor differences.

## Markdown ##

Docbuilder does not follow the Markdown specification completely, which may cause issues. (See [#27](https://github.com/shakna-israel/docbuilder/issues/27) and [#28](https://github.com/shakna-israel/docbuilder/issues/28).

However, generally speaking, it follows fairly closely.

In Docbuilder, all Markdown statements are encapsulated in Python Comments, in other words, they are proceeded by a '*#*'.

e.g.

A Markdown title usually appears as:

```
# Title
```

Would be written as:

```
# # Title
```

*Note: As it stands, the white space between the # denoting a Python comment, and the start of Markdown syntax does not matter, as it is stripped away. This may change in later versions.*

### Bullet Points

```
# * This is a bullet point
```

### Images

```
# [Image Alternative Text](Image link)
```

### Formatting

```
# *This is italic*

# **This is bold**

# ***This both italic and bold.***
```

### No formatting

A simple comment would appear as:

```
# This is a comment.
```

## Python ##

Python commands appear as normal, with their normal indentation.

So a simple Docbuilder Python Literate Program would be:

```
## Simple Literate Program
### A demonstration program

# This is a simple Hello World print statement.
print("Hello World!")
```

Which, when parsed by Docbuilder, would look like:

# Simple Literate Program

## A demonstration program

This is a simple Hello World print statement.

```
print("Hello World!")
```
