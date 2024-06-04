# -*- coding: ascii -*-
# multi_p.py

#import ray

import multiprocessing
import subprocess
from datasets import load_dataset
import asyncio

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

async def ocf(example)->None:
  process = await asyncio.create_subprocess_exec('clang','-O3','-c','-xir','-o','-','-', stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE, stdin=asyncio.subprocess.PIPE)

  stdout, stderr = await process.communicate(input=example)
  return None

def cp(example)->None:
  asyncio.run(ocf(example))
  return None

async def main():
    await asyncio.gather(*(ocf(x) for x in ds['content']))


#ds = load_dataset('llvm-ml/ComPile', split='train')
ds = load_dataset("llvm-ml/ComPile", split="train[0:1000]")

asyncio.run(main())
#ds = load_dataset("llvm-ml/ComPile", split="train[0:31653]")
#ds.map(cf, input_columns='content', num_proc=16)

#asyncio.run(ocf(x)) for x in ds['content']

