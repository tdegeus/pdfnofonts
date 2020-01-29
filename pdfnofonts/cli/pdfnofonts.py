'''pdfnofonts
    Convert (using GhostScript) PDFs such that all fonts are converted to outlines.

Usage:
    pdfnofonts [options] <files>...

Options:
    -s, --silent    Do not print any progress.
        --verbose   Verbose all commands.
    -h, --help      Show help.
        --version   Show version.

(c - MIT) T.W.J. de Geus | tom@geus.me | www.geus.me | github.com/tdegeus/pdfnofonts
'''

# --------------------------------------------------------------------------------------------------

import docopt
import sys

from .. import __version__
from .. import convert

# --------------------------------------------------------------------------------------------------
# main program
# --------------------------------------------------------------------------------------------------

def main():

    args = docopt.docopt(__doc__, version=__version__)

    for file in args['<files>']:

        try:
            convert(file, args['--verbose'])
        except Exception as e:
            print(str(e))
            sys.exit(1)

        if not args['--silent']:
            print('[pdfnofonts] "{0:s}"'.format(file))

# --------------------------------------------------------------------------------------------------
# command-line call
# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    main()
