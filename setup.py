#!/usr/bin/env python

import sys
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (2,5):
    raise NotImplementedError("Sorry, you need at least Python 2.5 or Python 3.x to use docbuilder.")

import docbuilder

setup(name='docbuilder',
      version=docbuilder.__version__,
      description='Python Literate Programming without Detanglement',
      long_description=docbuilder.__description__,
      author=docbuilder.__author__,
      author_email='jmilne@graphic-designer.com',
      url='http://docbuilder.rtfd.org/',
      py_modules=['docbuilder'],
      scripts=['docbuilder.py'],
      license='MIT',
      platforms = 'any',
     )
