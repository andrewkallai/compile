# -*- coding: ascii -*-


import subprocess
from datasets import load_dataset

ds = load_dataset("llvm-ml/ComPile", split="train[0:1000]")
  #subprocess.run(['clang','-O3','-c','-xir','-o','-','-'],input=example,capture_output=True).stdout
commands = ['clang','-O3','-c','-xir','-o','-','-']
p = [subprocess.run(commands, input=x, capture_output=True) for x in ds["content"]]

#with subprocess.Popen(
#    commands,
#    stdout=subprocess.PIPE,
#    stderr=subprocess.STDOUT,
#    stdin=subprocess.PIPE) as dis_process:
    #output = dis_process.communicate(
#      input=example)

#ds = load_dataset("llvm-ml/ComPile", split="train[0:31653]")

#with ThreadPoolExecutor(max_workers=4) as executor:

