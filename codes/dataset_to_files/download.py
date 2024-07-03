# -*- coding: ascii -*-
# download.py
from datasets import load_dataset

with parallel.parallel_backend('spark'):
  ds = load_dataset('llvm-ml/ComPile', split='train', num_proc=2)
  #ds = load_dataset("llvm-ml/ComPile", split="train[0:31653]", num_proc=2)
#ds = load_dataset('llvm-ml/ComPile', split='train', columns=['content'], num_proc=2)

