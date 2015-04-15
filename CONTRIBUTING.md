# Contributing

* Issues
    * If you find an issue, submit it on github. This might be a bug, it might be something you think Docbuilder should do, or just an idea.

* Pull Requests
    * If you make a change to the code - ensure there is a test for it in tests/test.py
    * Raise a request early. Even if the code isn't complete, it's better to talk it over earlier.
    * Don't make a pull request for something that isn't in Issues.
    * When making Pull Requests, make sure your fork is not on ```master```.
       * Preferably name your branch something relevant to the issue you are solving.
    * Before a pull request can be merged, it needs to pass all Travis-CI checks.
    * Before a pull request can be merged, it needs to comply with all Styleguides. (Check the [docs](https://docbuilder.readthedocs.org))

## Pre-requisites

Docbuilder has a few development dependencies, these can be installed with:

```
pip install -r tests/dev-requirements.txt
```
