# -*- coding: ascii -*-
# multi_p.py

#import ray

import multiprocessing
import subprocess
from datasets import load_dataset

#ray.init()

#@ray.remote

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
#ds = load_dataset("llvm-ml/ComPile", split="train[0:1000]")
ds = load_dataset("llvm-ml/ComPile", split="train[0:31653]")
#ds.map(cf, input_columns='content', num_proc=16)


cpus = multiprocessing.cpu_count()

def square(n):
    return n * n

#print(pool.map(square, range(1000)))
pool = multiprocessing.pool.ThreadPool(processes=cpus)
#pool = multiprocessing.Pool(processes=cpus)
pool.map(cf, ds['content'])
pool.close()
#ray.get([cf.remote(x) for x in ds['content']])
