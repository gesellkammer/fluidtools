#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, Extension
import sys
import os

VERSION = '0.2.0'

include_dirs = []
library_dirs = []
compile_args = []


def tree(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


if sys.platform == 'darwin':
    include_dirs.append("/usr/local/include/")
    include_dirs.append("/opt/local/include/")

    library_dirs.append("/usr/local/lib")
    library_dirs.append("/opt/local/lib")

    compile_args += [
        '-fno-strict-aliasing',
        '-Werror-implicit-function-declaration',
        '-Wfatal-errors'
    ]
elif sys.platform == 'linux':
    include_dirs.extend(['usr/include', '/usr/local/include'])
    library_dirs.append("/usr/local/lib")
    compile_args += [
        '-fno-strict-aliasing',
        '-Werror-implicit-function-declaration',
        '-Wfatal-errors'
    ]
else:
    import struct
    arch = 'x64' if 8 * struct.calcsize("P") == 64 else 'x86'
    triplet = f"{arch}-windows"
    include_dirs.append(os.path.expandvars(f"$VCPKG_ROOT\\installed\\{triplet}\\include"))
    library_dirs.append(os.path.expandvars(f"$VCPKG_ROOT\\installed\\{triplet}\\lib"))  
    root = os.path.expandvars(f"$VCPKG_ROOT")
    if os.path.exists(root):
        tree(root)
    else:
        print(">>>>>>>>>>>>>>>>>>>> Root path {root} does not exist!!")
        
setup(
    name='fluidtools',
    python_requires='>=3.8',
    version=VERSION,
    ext_modules=[
        Extension(
            'fluidtools', 
            sources = ['src/fluidtools.pyx'],
            libraries=['fluidsynth'],
            library_dirs=library_dirs,
            include_dirs=include_dirs,
            extra_compile_args=compile_args
        )
    ],
    setup_requires=['setuptools>=18', 'cython'],
    install_requires=['cython'],
    author='Eduardo Moguillansky',
    author_email='eduardo.moguillansky@gmail.com',
    maintainer='Eduardo Moguillansky',
    maintainer_email='eduardo.moguillansky@gmail.com',
    url='https://github.com/gesellkammer/fluidtools',
    description='Utilities to work with sounfonts',
    long_description='Utilities to work with soundfonts using fluidsynth',
    long_description_content_type='text/markdown',
    license='LGPL',
)
