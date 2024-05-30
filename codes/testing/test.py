# -*- coding: ascii -*-
# test.py
import subprocess
from datasets import load_dataset
from datasets import parallel

def add_prefix(example, idx):
  subprocess.run(['clang','-O3','-c','-xir','-o','-','-'],input=ds[idx]["content"],capture_output=True).stdout
  #print(example["language"])
  return example

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
#ds = load_dataset("llvm-ml/ComPile", split="train[0:31653]")
#ds = load_dataset("llvm-ml/ComPile", split="train[0:1000]")
#ds.map(add_prefix, with_indices=True, num_proc=4)
#ds.map(cf, input_columns='content', num_proc=128)

with parallel.parallel_backend('spark'):
  ds = load_dataset("llvm-ml/ComPile", split="train", num_proc=2)
  #dataset = load_dataset("llvm-ml/ComPile", split="train[0:1000]", num_proc=2)
