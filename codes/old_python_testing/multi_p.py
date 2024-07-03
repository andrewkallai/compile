# -*- coding: ascii -*-
# multi_p.py


import multiprocessing
import subprocess
from datasets import load_dataset, parallel


def cf(example)->None:
  #subprocess.run(['clang','-O3','-c','-xir','-o','-','-'],input=example,capture_output=True).stdout
  commands = ['clang','-O3','-c','-xir','-o','-','-']
  with subprocess.Popen(
    commands,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    stdin=subprocess.PIPE) as dis_process:
    output = dis_process.communicate(
      input=example)[0]
  return None 

#ds = load_dataset('llvm-ml/ComPile', split='train')
with parallel.parallel_backend('spark'):
  #ds = load_dataset("llvm-ml/ComPile", split="train[0:10]", num_proc=2)
  #ds = load_dataset("llvm-ml/ComPile", split="train[0:31653]", num_proc=2)
  ds = load_dataset("llvm-ml/ComPile", split="train", num_proc=2)


cpus = multiprocessing.cpu_count()

pool = multiprocessing.pool.ThreadPool(processes=cpus)
pool.map(cf, ds['content'][:1000])
pool.close()
