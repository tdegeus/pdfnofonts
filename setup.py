
from setuptools import setup
from setuptools import find_packages

import re

filepath = 'pdfnofonts/__init__.py'
__version__ = re.findall(r'__version__ = \'(.*)\'', open(filepath).read())[0]

setup(
    name = 'pdfnofonts',
    version = __version__,
    license = 'MIT',
    author = 'Tom de Geus',
    author_email = 'tom@geus.me',
    description = 'Script to remove fonts from PDF file (wrapper around GhostScript)',
    long_description = 'Script to remove fonts from PDF file (wrapper around GhostScript)',
    keywords = 'PDF, GhostScript',
    url = 'https://github.com/tdegeus/pdfnofonts',
    packages = find_packages(),
    install_requires = ['docopt>=0.6.2'],
    entry_points = {
        'console_scripts': ['pdfnofonts = pdfnofonts.cli.pdfnofonts:main']})
