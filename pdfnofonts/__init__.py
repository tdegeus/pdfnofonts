'''pdfnofonts
  Convert PDF to PDF where all fonts are converted to outlines.

Usage:
  pdfnofonts [options] <files>...

Options:
  -s, --silent    Do not print any progress.
      --verbose   Verbose all commands.
  -h, --help      Show help.
      --version   Show version.

(c - MIT) T.W.J. de Geus | tom@geus.me | www.geus.me
'''

# ========================================= LOAD LIBRARIES =========================================

import sys
import os
import re
import docopt
import subprocess
import shutil
import tempfile

import pkg_resources

__version__ = pkg_resources.require("pdfnofonts")[0].version

# ==================================== RAISE COMMAND LINE ERROR ====================================

def Error(msg,exit_code=1):

  print(msg)

  sys.exit(exit_code)

# ========================================== RUN COMMAND ===========================================

def Run(cmd,verbose=False,**kwargs):

  out = subprocess.check_output(cmd,shell=True).decode('utf-8')

  if verbose:
    print(cmd)
    print(out,end='')

  return out

# ========================================== MAIN PROGRAM ==========================================

def main():

  # ---------------------------------- parse command line arguments ----------------------------------

  # parse command-line arguments
  args = docopt.docopt(__doc__, version=__version__)

  # change keys to simplify implementation:
  # - remove leading "-" and "--" from options
  args = {re.sub(r'([\-]{1,2})(.*)',r'\2',key): args[key] for key in args}
  # - change "-" to "_" to facilitate direct use in print format
  args = {key.replace('-','_'): args[key] for key in args}
  # - remove "<...>"
  args = {re.sub(r'(<)(.*)(>)',r'\2',key): args[key] for key in args}

  # --------------------------------------------- check ----------------------------------------------

  # required command
  if not shutil.which('gs'):
    Error('"gs" not found')

  # check that files exist
  for file in args['files']:
    if not os.path.isfile(file):
      Error('"%s" does not exist' % file)

  # -------------------------------------------- convert ---------------------------------------------

  # loop over input files
  for file in args['files']:

    # get filename of a temporary file, in a unique temporary directory
    tempFile = os.path.join(tempfile.mkdtemp(), 'pdfnofonts.pdf')

    # move input to temporary file
    # - execute
    shutil.move(file, tempFile)
    # - verbose
    if args['verbose']: print('mv "{file:s}" "{tempFile:s}"'.format(file=file, tempFile=tempFile))

    # remove font using "gs"
    # - set command
    cmd = 'gs -o "{file:s}" -dNoOutputFonts -sDEVICE=pdfwrite "{tempFile:s}"'.format(tempFile=tempFile, file=file)
    # - verbose & execute
    Run(cmd,**args)

    # remove temporary file and directory
    # - execute
    shutil.rmtree(os.path.split(tempFile)[0])
    # - verbose
    if args['verbose']: print('rm -r "{tempFile:s}"'.format(tempFile=tempFile))

    # print progress
    if not args['silent']: print('[pdfnofonts] "{file:s}"'.format(file=file))
