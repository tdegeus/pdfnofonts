
from setuptools import setup

setup(
    name = 'pdfnofonts',
    version = '0.0.2',
    license = 'MIT',
    author = 'Tom de Geus',
    author_email = 'tom@geus.me',
    description = 'Script of remove fonts from PDF file (wrapper around GhostScript)',
    long_description = 'Script of remove fonts from PDF file (wrapper around GhostScript)',
    keywords = 'PDF, GhostScript',
    url = 'https://github.com/tdegeus/pdfnofonts',
    packages = ['pdfnofonts'],
    install_requires = ['docopt>=0.6.2',],
    entry_points = {
        'console_scripts': ['pdfnofonts = pdfnofonts:main']})
