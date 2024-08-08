# -*- coding: ascii -*-
from datasets import load_dataset, parallel
import os
import tarfile

bytes_list: [bytes]
lang_list: [str]
langs: [str]
MAX_JOBS: [int] = 400-1-299
STORAGE: [str] = '/lustre/schandra_crpl/users/3302/ir_bc_files/test_storage/'
with parallel.parallel_backend('spark'):
  dataset=load_dataset('llvm-ml/ComPile', split='train[0:301]', num_proc=2)
#  dataset=load_dataset('llvm-ml/ComPile', split='train', num_proc=2)
#bytes_list, lang_list=dataset["content"], dataset["language"]
lang_list=dataset["language"]
langs=dataset.unique("language")
#  bytes_list=load_dataset('llvm-ml/ComPile', split='train[0:31653]', num_proc=2)["content"]
for i in range(0, len(langs)):
  start_index=lang_list.index(langs[i])
  if (i+1 != len(langs)):
    end_index=lang_list.index(langs[i+1])
  else:
    end_index=len(lang_list)
  batch_size=(end_index-start_index)//MAX_JOBS
  print(start_index, end_index, batch_size, flush=True)
  for j in range(start_index, end_index, batch_size):
#    bytes_list=dataset.select(range(j, j+batch_size-1))["content"]
    dir_name = os.path.join(STORAGE, f'{STORAGE}{langs[i]}/{j}_temp')
    os.makedirs(dir_name, exist_ok=True)
    for index in range(j, j+batch_size if (j+batch_size <= end_index) else end_index):
      filename = f'{dir_name}/file{index}.bc'
      with open(filename, 'wb') as file:
        file.write(dataset[index]["content"])
      with tarfile.open(f'{dir_name}/{langs[i]}_{j}.tar', "a") as tar:
        tar.add(filename, arcname=f'bc_files/file{index}.bc')
      os.remove(filename)
    

#  for index, byte_item in enumerate(bytes_list, start=1):


