# -*- coding: ascii -*-

from joblib import Parallel, delayed
import subprocess
from datasets import load_dataset
from math import sqrt


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

ds = load_dataset("llvm-ml/ComPile", split="train[0:1000]")
#ds = load_dataset("llvm-ml/ComPile", split="train[0:31653]")
#ds.map(cf, input_columns='content', num_proc=16)
Parallel(n_jobs=-1, prefer="threads")(
    delayed(cf)(i) for i in ds["content"])



