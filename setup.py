from setuptools import setup

setup(name='brewls',
      version='0.2',
      description='A better homebrew package search',
      url='http://github.com/kkatayama',
      author='Teddy',
      author_email='katayama@udel.edu',
      license='MIT',
      packages=['brewls'],
      python_requires='>=3',
      scripts=['bin/brewls'],
      zip_safe=False)
