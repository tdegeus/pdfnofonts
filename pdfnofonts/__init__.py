
import os
import subprocess
import shutil
import tempfile

__version__ = '1.1.0'

# --------------------------------------------------------------------------------------------------
# Run command (and verbose it), and return the command's output
# --------------------------------------------------------------------------------------------------

def run(cmd, verbose=False):
    r'''
Run command, optionally verbose command and output, and return output.
    '''

    out = subprocess.check_output(cmd, shell=True).decode('utf-8')

    if verbose:
        print(cmd)
        print(out)

    return out

# --------------------------------------------------------------------------------------------------
# Apply conversion: fonts -> outlines
# --------------------------------------------------------------------------------------------------

def convert(file, verbose=False):
    r'''
Convert (using GhostScript) PDFs such that all fonts are converted to outlines.

:arguments:

    **file** (``<str>``)
        File-name.

:options:

    **verbose** ([``False``] | ``True``)
        Verbose all commands and their output.
    '''

    if not shutil.which('gs'):
        raise IOError('"gs" not found')

    if not os.path.isfile(file):
        raise IOError('"{0:s}" does not exist'.format(file))

    temp_dir = tempfile.mkdtemp()
    temp_pdf = os.path.join(temp_dir, 'pdfnofonts.pdf')

    cmd = 'gs -o "{0:s}" -dNoOutputFonts -sDEVICE=pdfwrite "{1:s}"'.format(temp_pdf, file)

    run(cmd, verbose)

    shutil.move(temp_pdf, file)

    if verbose:
        print('mv "{0:s}" "{1:s}"'.format(temp_pdf, file))

    shutil.rmtree(temp_dir)
