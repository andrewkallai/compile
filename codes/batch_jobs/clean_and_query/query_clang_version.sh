#!/bin/bash
PREFIX=/home/3302/hf_py_code/compile/csv_data/
clang --version > ${PREFIX}clang_version.txt 
git --git-dir=/lustre/schandra_crpl/sw/LLVM/llvm-project/.git log | grep -m 1 "commit" >> ${PREFIX}clang_version.txt
