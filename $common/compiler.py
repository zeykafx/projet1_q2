#!/usr/bin/python3
# -*- coding: utf-8 -*-


import py_compile
import sys
import os


def compile_student_files(dir):
    for file in os.listdir(dir):
        if(file.endswith('.py') and file != 'compiler.py'):
            py_compile.compile(dir + file, './student/' + file + 'c')


if __name__ == '__main__':
    compile_student_files(sys.argv[1])
