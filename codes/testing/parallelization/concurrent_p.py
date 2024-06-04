# -*- coding: ascii -*-


import subprocess
from datasets import load_dataset
from concurrent.futures import ThreadPoolExecutor, as_completed

def cf(example)->None:
  #subprocess.run(['clang','-O3','-c','-xir','-o','-','-'],input=example,capture_output=True).stdout
  commands = ['clang','-O3','-c','-xir','-o','-','-']
  with subprocess.Popen(
    commands,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    stdin=subprocess.PIPE) as dis_process:
    output = dis_process.communicate(
      input=example)
  return None 

ds = load_dataset("llvm-ml/ComPile", split="train[0:1000]")
#ds = load_dataset("llvm-ml/ComPile", split="train[0:31653]")

#with ThreadPoolExecutor(max_workers=4) as executor:
with ThreadPoolExecutor() as executor:
        futures = {executor.submit(cf, x): x for x in ds["content"]}

