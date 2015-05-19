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
      classifiers=['Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approvied :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python 2.7',
        'Programming Language :: Python 3.2',
        'Programming Language :: Python 3.3',
        'Programming Language :: Python 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Documentation',
        'Topic :: Scientific/Engineering',
        'Topic :: Text Processing'
     )
