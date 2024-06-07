# -*- coding: ascii -*-
from datasets import load_dataset, parallel
bytes_list: [bytes]
with parallel.parallel_backend('spark'):
  bytes_list=load_dataset('llvm-ml/ComPile', split='train[0:31653]', num_proc=2)["content"]
  bytes_list=load_dataset('llvm-ml/ComPile', split='train[31653:87225]', num_proc=2)["content"]
  bytes_list=load_dataset('llvm-ml/ComPile', split='train[87225:144641]', num_proc=2)["content"]
  bytes_list=load_dataset('llvm-ml/ComPile', split='train[144641:209641]', num_proc=2)["content"]
  bytes_list=load_dataset('llvm-ml/ComPile', split='train[209641:274641]', num_proc=2)["content"]
  bytes_list=load_dataset('llvm-ml/ComPile', split='train[274641:339641]', num_proc=2)["content"]
  bytes_list=load_dataset('llvm-ml/ComPile', split='train[339641:353700]', num_proc=2)["content"]
  bytes_list=load_dataset('llvm-ml/ComPile', split='train[353700:402751]', num_proc=2)["content"]


for index, byte_item in enumerate(bytes_list[:3], start=1):
  filename = f'/lustre/schandra_crpl/users/3302/ir_bc_files/file{index}.bc'
    
  with open(filename, 'wb') as file:
    file.write(byte_item)
  #print(f"Bytes have been written to group")

