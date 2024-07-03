#!/usr/bin/env python3
# -*- coding: ascii -*-
# load_data.py


from datasets import load_dataset

def datal():
  return load_dataset('llvm-ml/ComPile', split='train')

def writebc(index: int, ds):
  binary_file = open("find_text.bc", "wb")
  binary_file.write(ds[index]["content"])
  binary_file.close()

