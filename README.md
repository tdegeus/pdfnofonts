# pdfnofonts

[![Travis](https://travis-ci.org/tdegeus/pdfnofonts.svg?branch=master)](https://travis-ci.org/tdegeus/pdfnofonts)
[![Build status](https://ci.appveyor.com/api/projects/status/olcapcdgsfnp1wj4?svg=true)](https://ci.appveyor.com/project/tdegeus/pdfnofonts)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/pdfnofonts.svg)](https://anaconda.org/conda-forge/pdfnofonts)

Command that wraps around GhostScript to remove all fonts from a PDF and convert them into outlines.

```none
pdfnofonts [options] <files>...
```

Note that the script is in fact a simple Python script that wraps GhostScript. 

# Contents

<!-- MarkdownTOC -->

- [Disclaimer](#disclaimer)
- [Getting pdfnofonts](#getting-pdfnofonts)
    - [Using conda](#using-conda)
    - [Using PyPi](#using-pypi)
    - [From source](#from-source)
- [Usage](#usage)

<!-- /MarkdownTOC -->

# Disclaimer 

This library is free to use under the [MIT license](https://github.com/tdegeus/pdfnofonts/blob/master/LICENSE). Any additions are very much appreciated, in terms of suggested functionality, code, documentation, testimonials, word-of-mouth advertisement, etc. Bug reports or feature requests can be filed on [GitHub](https://github.com/tdegeus/pdfnofonts). As always, the code comes with no guarantee. None of the developers can be held responsible for possible mistakes.

Download: [.zip file](https://github.com/tdegeus/pdfnofonts/zipball/master) | [.tar.gz file](https://github.com/tdegeus/pdfnofonts/tarball/master).

(c - [MIT](https://github.com/tdegeus/pdfnofonts/blob/master/LICENSE)) T.W.J. de Geus (Tom) | tom@geus.me | www.geus.me | [github.com/tdegeus/pdfnofonts](https://github.com/tdegeus/pdfnofonts)

# Getting pdfnofonts

## Using conda

```bash
conda install -c conda-forge pdfnofonts
```

This will also install all necessary dependencies.

## Using PyPi

```bash
pip install pdfnofonts
```

This will also install the necessary Python modules, **but not GhostScript**.

## From source

```bash
# Download pdfnofonts
git checkout https://github.com/tdegeus/pdfnofonts.git
cd pdfnofonts

# Install
python -m pip install .
```

This will also install the necessary Python modules, **but not GhostScript**.

# Usage

The usage is as follows (see `pdfnofonts --help`):

```none
pdfnofonts
  Convert PDF to PDF where all fonts are converted to outlines.

  Note that this command is a wrapper around GhostScript.

Usage:
  pdfnofonts [options] <files>...

Options:
  -s, --silent    Do not print any progress.
      --verbose   Verbose all commands.
  -h, --help      Show help.
      --version   Show version.
```
