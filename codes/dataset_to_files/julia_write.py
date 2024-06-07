# -*- coding: ascii -*-
from datasets import load_dataset, parallel
bytes_list: [bytes]
with parallel.parallel_backend('spark'):
  bytes_list=load_dataset('llvm-ml/ComPile', split='train[87225:144641]', num_proc=2)["content"]


for index, byte_item in enumerate(bytes_list, start=87226):
  filename = f'/lustre/schandra_crpl/users/3302/ir_bc_files/julia/file{index}.bc'
    
  with open(filename, 'wb') as file:
    file.write(byte_item)
  #print(f"Bytes have been written to group")

