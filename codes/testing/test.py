# -*- coding: ascii -*-
# test.py
import subprocess, multiprocessing
from datasets import load_dataset, parallel

with parallel.parallel_backend('spark'):
  #ds = load_dataset('llvm-ml/ComPile', split='train[0:100688]', num_proc=2)
  ds = load_dataset('llvm-ml/ComPile', split='train', num_proc=2)
print(ds.num_rows)
#ds["content"]
  #binary_file = open("file2.bc", "wb")
  #binary_file.write(ds["content"][1])
  #binary_file.close()
