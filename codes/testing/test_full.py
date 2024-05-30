#!/usr/bin/env python3
# -*- coding: ascii -*-
# test_full.py

from datasets import load_dataset
import subprocess
import sys
import threading


ds = load_dataset('llvm-ml/ComPile', split='train')
CC='clang++'
OPT='-O1'

def compile_and_measure(iteration: int):
      o=subprocess.run([CC,OPT,'-c','-xir','-o','-','-'],input=ds[iteration]["content"],capture_output=True).stdout
      return [elapsed_time, size, ds[iteration]["package_source"], iteration]

def create_list(start, end, var):
  var.extend([compile_and_measure(i) for i in range(start, end)])

#for i in range(12032, 13056)
parent_list = []
if (CC == 'clang'):
  MAX=12032
  NUM_THREADS=12
  OFFSET=0
else:
  MAX=1025
  NUM_THREADS=4
  OFFSET=12032

INTERVAL = int(MAX / NUM_THREADS)
EXTRA = MAX % NUM_THREADS
threads = []
for i in range(0, NUM_THREADS):
    if(i == NUM_THREADS -1):
      thread = threading.Thread(target=create_list, args=(OFFSET+i*INTERVAL,OFFSET+(i+1)*INTERVAL+EXTRA,parent_list))
    else:
      thread = threading.Thread(target=create_list, args=(OFFSET+i*INTERVAL,OFFSET+(i+1)*INTERVAL,parent_list))

    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

parent_list.sort()

#for i in range(0, 12032)
#for i in range(12032, 13056)
