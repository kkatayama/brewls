"""
A Better HomeBrew Package Search

Usage: brewls [keyword]

"""

from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='brewls',
      version='1.0.1',
      description='A better homebrew package search',
      url='http://github.com/kkatayama/brewls',
      author='Teddy',
      author_email='katayama@udel.edu',
      license='MIT',
      packages=['brewls'],
      python_requires='>=3',
      scripts=['bin/brewls'],
      install_requires=required,
      zip_safe=False)
