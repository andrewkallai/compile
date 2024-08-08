# -*- coding: ascii -*-
from datasets import load_dataset, parallel
import os
#import tarfile
import multiprocessing
import csv

bytes_list: [bytes]
lang_list: [str]
#global langs
STORAGE: [str] = '/tmp/test_storage'
#global i
#global j
global dir_name
BATCH_SIZE: int = 15000
file_indices: [dict] = []


def write_file(index: [int], bytes_item: [bytes]):
      filename = f'{dir_name}/file{index+1}.bc'
      with open(filename, 'wb') as file:
        file.write(bytes_item)
#      with tarfile.open(f'{dir_name}/{langs[i]}_{j}.tar', "a") as tar:
#        tar.add(filename, arcname=f'bc_files/file{index+j}.bc')
#      os.remove(filename)

with parallel.parallel_backend('spark'):
  dataset=load_dataset('llvm-ml/ComPile', split='train', num_proc=2)
#  dataset=load_dataset('llvm-ml/ComPile', split='train[0:31653]', num_proc=2)
lang_list=dataset["language"]
langs=dataset.unique("language")
pool = multiprocessing.pool.ThreadPool(processes=multiprocessing.cpu_count())
for i in range(0, len(langs)):
  start_index=lang_list.index(langs[i])
  if (i+1 != len(langs)):
    end_index=lang_list.index(langs[i+1])
  else:
    end_index=len(lang_list)
  file_indices.append({"language": langs[i], "start_index": start_index, "end_index": end_index})
  print(start_index, end_index, BATCH_SIZE, flush=True)
  for j in range(start_index, end_index, BATCH_SIZE):
    dir_name = os.path.join(STORAGE, f'{STORAGE}/{langs[i]}/{j}_temp')
    os.makedirs(dir_name, exist_ok=True)
    pool.starmap(write_file, enumerate(dataset[j:j+BATCH_SIZE if (j+BATCH_SIZE <= end_index) else end_index]['content']))

pool.close()
    
with open('indices.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["language", "start_index", "end_index"], dialect='unix', quoting=csv.QUOTE_NONE)
    writer.writeheader()
    writer.writerows(file_indices)

