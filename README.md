# Docbuilder

![Release](https://img.shields.io/github/tag/shakna-israel/docbuilder.svg) [![Build](https://travis-ci.org/shakna-israel/docbuilder.svg)](https://travis-ci.org/shakna-israel/docbuilder/) 

[![Issues](https://img.shields.io/github/issues/shakna-israel/docbuilder.svg)](https://github.com/shakna-israel/docbuilder/issues)

[![Python Versions](https://img.shields.io/badge/Python-2.6%2C%202.7%2C%203.2%2C%203.3%2C%203.4%2C%20PyPy%2C%20PyPy3%2C%20Cython-blue.svg)](https://github.com/shakna-israel/docbuilder/issues/12) ![License](https://img.shields.io/badge/license-MIT-blue.svg)

* Docbuilder is a small python script that will take another Python program, and turn it into documentation.
    * This is the [Literate Programming Style](https://github.com/jashkenas/journo)
* Docbuilder is used to generate technical documentation. *It isn't reccomended at this stage for User Documentation.*
* It generates Markdown documents, though it does expect that MKDocs will use it.

## Usage

Check the [Public API](API.md)

Or, if you just want a quickstart:

```
python docbuilder.py -i mypthonlit.pylit -o mydoc
```

## Python Versions

Currently, the supported versions of Python are: [![Python Versions](https://img.shields.io/badge/Python-2.6%2C%202.7%2C%203.2%2C%203.3%2C%203.4%2C%20PyPy%2C%20PyPy3%2C%20Cython-blue.svg)](https://github.com/shakna-israel/docbuilder/issues/12)

*Check [Python Compatibility](https://github.com/shakna-israel/docbuilder/issues/12) for more information.*

## Testing

[![Throughput Graph](https://graphs.waffle.io/shakna-israel/docbuilder/throughput.svg)](https://waffle.io/shakna-israel/docbuilder/metrics)

[![Codeship](https://codeship.com/projects/320ce4c0-c272-0132-53d4-36229af8a5d4/status?branch=master)](https://codeship.com/projects/73757)

[![Code Health](https://landscape.io/github/shakna-israel/docbuilder/master/landscape.svg?style=flat)](https://landscape.io/github/shakna-israel/docbuilder/master)
