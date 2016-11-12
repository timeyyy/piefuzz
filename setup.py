import os
from setuptools import setup
from distutils.command.install import INSTALL_SCHEMES

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(name='piefuzz',
      version='1.0.3',
      description="Pie wrapper for junegunn's fuzzyfinder (fzf)",
      long_description = read('README.md'),
      keywords = 'pyfzf fzf fuzzyfinder fuzz find ctrl-p command-t',
      author='timothy c eiechler',
      author_email='timeyyy_da_man@hotmail.com',
      license='MIT',
      url='https://github.com/timeyyy/piefuzz',
      install_requires=['plumbum'],
      py_modules=['piefuzz'],
	  packages=['piefuzz'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Terminals',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          ]
      )

