"""
Usage : run this script in the main source folder of the cpython source
    code, with as a first argument, the location of the windows headers

Eg ::

    python3 windows_headers.py /usr/x86_64-w64-mingw32/include/
"""

import glob
import os
import sys

if not len(sys.argv[1]):
    raise Exception('Please specify path to windows headers as first argument')

print('looking in {0}'.format(sys.argv[1]))

#
# Create list of windows headers
#

headers = set()
for p in glob.glob(os.path.join(sys.argv[1], '**', '*.h'), recursive=True):
    basename = os.path.basename(p)
    headers.add(basename.lower())

if 'windows.h' in headers:
    print('windows headers found')
else:
    raise Exception('This path does not contain windows headers')

print(len(headers), 'windows headers found')

#
# Exclude standard headers
#

for p in glob.glob(os.path.join('/usr/include/', '**', '*.h'), recursive=True):
    basename = os.path.basename(p)
    headers.discard(basename.lower())

print(len(headers), 'after removing standard headers :')

for header in sorted(list(headers)):
    print(header)
#
# Create list of sources
#

sources = []
for p in glob.glob(os.path.join('.', '**', '*.c'), recursive=True):
    rel_path = os.path.relpath(p, '.')
    sources.append(rel_path)
for p in glob.glob(os.path.join('.', '**', '*.h'), recursive=True):
    rel_path = os.path.relpath(p, '.')
    sources.append(rel_path)

if os.path.join('Programs', 'python.c') in sources:
    print('python source found')
else:
    raise Exception('This script should run in the main folder of the cpython sources')

#
# Validate sources
#

total_count = 0
for source in sources:
    source_text = open(source).readlines()
    include_lines = [(i, line) for i, line in enumerate(source_text) if '#include' in line]
    header_count = 0
    for header in headers:
        for i, line in include_lines:
            if header in line.lower():
                header_count += 1
                if header not in line:
                    print(source, header, i+1, line)
    total_count += header_count
    if header_count > 0:
        print(source, ':', header_count)
print('total : ', total_count)