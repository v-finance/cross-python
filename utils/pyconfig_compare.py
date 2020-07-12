"""
Compare two pyconfig.h configuration files

python3 path/to/pyconfig1.h path/to/pyconfig2.h
"""

import difflib
import sys

if not len(sys.argv[1])!=2:
    raise Exception('Please specify 2 paths to pyconfig.h files')

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
    
defined_1 = read_pyconfig(sys.argv[1])
defined_2 = read_pyconfig(sys.argv[2])

for defined in defined_1:
    if defined in defined_2:
        print('both ', defined)
        defined_1.remove(defined)
        defined_2.remove(defined)

differ = difflib.Differ()

for diffline in differ.compare(defined_1, defined_2):
    print(diffline)