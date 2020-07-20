"""
Compare two pyconfig.h configuration files

python3 path/to/pyconfig1.h path/to/pyconfig2.h
"""

import difflib
import sys

if not len(sys.argv[1])!=2:
    raise Exception('Please specify reference and tested pyconfig.h files')

def read_pyconfig(p):
    print('reading {0}'.format(p))
    source_text = open(p).readlines()
    define_lines = [line for line in source_text if line.startswith('#define')]
    defined = []
    for define_line in define_lines:
        define_parts = define_line.split(' ')
        if len(define_parts)>=2:
            defined.append(define_parts[1].strip())
    defined.sort()
    return defined
    
reference = read_pyconfig(sys.argv[1])
tested = read_pyconfig(sys.argv[2])

for defined in reference:
    if defined in tested:
        print('both', defined)
        while defined in reference:
            reference.remove(defined)
        while defined in tested:
            tested.remove(defined)

for defined in reference:
    if defined not in tested:
        print('missing', defined)