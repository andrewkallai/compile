# -*- coding: ascii -*-
# multi_p.py


#import multiprocessing
#import subprocess
from subprocess import Popen, PIPE
from datasets import load_dataset


#def cf(example)->None:
  #subprocess.run(['clang','-O3','-c','-xir','-o','-','-'],input=example,capture_output=True).stdout
#  commands = ['clang','-O3','-c','-xir','-o','-','-']
#  with subprocess.Popen(
#    commands,
#    stdout=subprocess.PIPE,
#    stderr=subprocess.STDOUT,
#    stdin=subprocess.PIPE) as dis_process:
#    output = dis_process.communicate(
#      input=example)[0]
#  return None 


#ds = load_dataset('llvm-ml/ComPile', split='train')
ds = load_dataset("llvm-ml/ComPile", split="train[0:1000]")

#ds = load_dataset("llvm-ml/ComPile", split="train[0:31653]")

commands = ['clang','-O3','-c','-xir','-o','-','-']

for x in ds["content"]:
  with Popen(commands, stdout=PIPE, stderr=PIPE, stdin=PIPE) as proc:

for p in procs:
    p.communicate(input=x)
    p.wait()

#.communicate(input=x).wait

#cpus = multiprocessing.cpu_count()

#pool = multiprocessing.pool.ThreadPool(processes=cpus)
#pool = multiprocessing.Pool(processes=cpus)
#pool.map(cf, ds['content'])
#pool.close()
