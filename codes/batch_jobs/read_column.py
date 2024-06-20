# -*- coding: ascii -*-
import csv

#PREFIX: str = "/lustre/schandra_crpl/users/3302/ir_bc_files/"
PREFIX: str = "/home/3302/hf_py_code/compile/codes/batch_jobs/"

textseg_data: [int] = []
inst_data: [int] = []
with open(PREFIX+"text_segments.csv", mode='r', newline='') as file:
  for x in csv.DictReader(file):
    textseg_data.append(int(x["text_segment_size"]))

with open(PREFIX+"instructions.csv", mode='r', newline='') as file:
  for x in csv.DictReader(file):
    inst_data.append(int(x["instructions"]))

#print(textseg_data)
