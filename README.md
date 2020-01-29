# pdfnofonts

[![Travis](https://travis-ci.org/tdegeus/pdfnofonts.svg?branch=master)](https://travis-ci.org/tdegeus/pdfnofonts)
[![Build status](https://ci.appveyor.com/api/projects/status/olcapcdgsfnp1wj4?svg=true)](https://ci.appveyor.com/project/tdegeus/pdfnofonts)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/pdfnofonts.svg)](https://anaconda.org/conda-forge/pdfnofonts)


Simple module to convert (using GhostScript) PDFs such that all fonts are converted to outlines.

## Command-line script 

```none
pdfnofonts [options] <files>...
```

## Python module

```python
import pdfcnofonts
pdfnofonts.combine(...)
```

# Contents

<!-- MarkdownTOC -->

- [Disclaimer](#disclaimer)
- [Getting pdfnofonts](#getting-pdfnofonts)
  - [Using conda](#using-conda)
  - [Using PyPi](#using-pypi)
  - [From source](#from-source)
- [Usage](#usage)
- [Usage from Python](#usage-from-python)
  - [Basic usage](#basic-usage)
  - [Arguments](#arguments)
  - [Options](#options)

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

This will install all necessary dependencies.

## Using PyPi

```bash
pip install pdfnofonts
```

This will install the necessary Python modules, **but not GhostScript**.

## From source

```bash
# Download pdfnofonts
git checkout https://github.com/tdegeus/pdfnofonts.git
cd pdfnofonts

# Install
python -m pip install .
```

This will install the necessary Python modules, **but not GhostScript**.

# Usage

The usage is as follows (see `pdfnofonts --help`):

```none
Usage:
    pdfnofonts [options] <files>...

Options:
    -s, --silent    Do not print any progress.
        --verbose   Verbose all commands.
    -h, --help      Show help.
        --version   Show version.
```

# Usage from Python

## Basic usage

```python
import pdfnofonts
pdfnofonts.combine(...)
```

## Arguments

+   `file` (`<str>`)
    
    PDF file.

## Options

+   `verbose` (**`False`** | `True`)
    
    Verbose all commands and their output.

