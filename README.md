piefuzz
=======

##### A python wrapper for *junegunn*'s awesome [fzf](https://github.com/junegunn/fzf).

This is a fork from pyfzf, the main difference is we operate in a non interactive mode.
We also work exclusivley on python3, instead of exclusivley on python2...

Requirements
------------

* Python 3.4+
* [fzf](https://github.com/junegunn/fzf)


Installation
------------
	pip install piefuzz

Usage
-----
    >>> from piefuzz import Fzf
    >>> fzf = Fzf()

Defaults to searching the path for fzf, you may also specify a path

A SystemError is thrown if fzf cannot be found

    >>> fzf = Fzf(fzf_path='/here/fzf')


To fuzz through a file with items seperated by newlines

    >>> result = fzf.fuzz(query, input_path='path/to/file.txt')

otherwise an iterable of strings

    >>> result = fzf.fuzz(query, input_list=['abc', 'def'])

output is a newline deliminated utf-8 string


License
-------
MIT

Thanks
------
This project makes use of [plumbum](http://plumbum.readthedocs.org/) to interact with [fzf](https://github.com/junegunn/fzf).

Definitley check it out nice stuff!
