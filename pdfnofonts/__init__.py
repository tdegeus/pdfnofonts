'''pdfnofonts
  Convert PDF to PDF where all fonts are converted to outlines.

  Note that this command is a wrapper around GhostScript.

Usage:
  pdfnofonts [options] <files>...

Options:
  -s, --silent    Do not print any progress.
      --verbose   Verbose all commands.
  -h, --help      Show help.
      --version   Show version.

(c - MIT) T.W.J. de Geus | tom@geus.me | www.geus.me
'''

# ==================================================================================================

import sys
import os
import re
import docopt
import subprocess
import shutil
import tempfile

__version__ = '1.0.1'

# --------------------------------------------------------------------------------------------------
# Command-line error: show message and quit with exit code "1"
# --------------------------------------------------------------------------------------------------

def Error(text):

    print(text)
    sys.exit(1)

# --------------------------------------------------------------------------------------------------
# Run command (and verbose it), and return the command's output
# --------------------------------------------------------------------------------------------------

def Run(cmd, verbose=False):

    out = subprocess.check_output(cmd, shell=True).decode('utf-8')

    if verbose:
        print(cmd)
        print(out)

    return out

# --------------------------------------------------------------------------------------------------
# Apply conversion: fonts -> outlines
# --------------------------------------------------------------------------------------------------

def ConvertFile(file, verbose=False):

    tempFile = os.path.join(tempfile.mkdtemp(), 'pdfnofonts.pdf')

    cmd = 'gs -o "{0:s}" -dNoOutputFonts -sDEVICE=pdfwrite "{1:s}"'.format(tempFile, file)
    Run(cmd, verbose)

    shutil.move(tempFile, file)
    if verbose:
        print('mv "{0:s}" "{1:s}"'.format(tempFile, file))

    shutil.rmtree(os.path.split(tempFile)[0])

# --------------------------------------------------------------------------------------------------
# main program
# --------------------------------------------------------------------------------------------------

def main():

    args = docopt.docopt(__doc__, version=__version__)

    if not shutil.which('gs'):
        Error('"gs" not found')

    for file in args['<files>']:
        if not os.path.isfile(file):
            Error('"{0:s}" does not exist'.format(file))

    for file in args['<files>']:

        ConvertFile(file, args['--verbose'])

        if not args['--silent']:
            print('[pdfnofonts] "{0:s}"'.format(file))
