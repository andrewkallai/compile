from datasets import load_dataset, parallel
import os
import multiprocessing
import csv
from sys import argv

# Usage:
# python write_data_files.py [STORAGE]

STORAGE: str
if len(argv) > 1:
    STORAGE = argv[1]
else:
    STORAGE = '/tmp'

lang_list: [str]
BATCH_SIZE: int = 15000
file_indices: [dict] = []


def write_file(index: [int], bytes_and_dir: (bytes, str)):
    filename = f'{bytes_and_dir[1]}/file{index+1}.bc'
    with open(filename, 'wb') as file:
        file.write(bytes_and_dir[0])


with parallel.parallel_backend('spark'):
    dataset = load_dataset('llvm-ml/ComPile', split='train', num_proc=2)
#    dataset = load_dataset('llvm-ml/ComPile', split='train[0:10]', num_proc=2)

lang_list = dataset["language"]
langs = dataset.unique("language")
pool = multiprocessing.pool.ThreadPool(processes=multiprocessing.cpu_count())

for i in range(0, len(langs)):
    start_index = lang_list.index(langs[i])
    if (i+1 != len(langs)):
        end_index = lang_list.index(langs[i+1])
    else:
        end_index = len(lang_list)
    file_indices.append(
        {"language": langs[i], "start_index": start_index, "end_index": end_index})
    with open('indices.csv', mode='w', newline='') as file:
      writer = csv.DictWriter(file, fieldnames=[
                            "language", "start_index", "end_index"], dialect='unix', quoting=csv.QUOTE_NONE)
      writer.writeheader()
      writer.writerows(file_indices)

pool.close()
quit()
for i in range(0, len(file_indices)):
    start_index = file_indices[i]["start_index"]
    end_index = file_indices[i]["end_index"]
    for j in range(start_index, end_index, BATCH_SIZE):
        dir_name = os.path.join(STORAGE, f'{STORAGE}/{file_indices[i]["language"]}/{j}_temp')
        os.makedirs(dir_name, exist_ok=True)
        bytes_enumeration = enumerate(
            [(bytes_item, dir_name) for bytes_item in dataset[j:j+BATCH_SIZE if (j+BATCH_SIZE <= end_index) else end_index]['content']], start=j)
        pool.starmap(write_file, bytes_enumeration)

pool.close()


