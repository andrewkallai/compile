# -*- coding: ascii -*-
# test.py
import subprocess, multiprocessing
from datasets import load_dataset, parallel

with parallel.parallel_backend('spark'):
  ds = load_dataset('llvm-ml/ComPile', split='train[0:1000]', num_proc=2)
