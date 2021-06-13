#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, Extension
import sys

VERSION = '0.2.0'

include_dirs = []
library_dirs = []
compile_args = []

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
    pass


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
