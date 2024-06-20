# -*- coding: ascii -*-
import csv

def open_and_load(lang: str):
  PREFIX:str="/home/3302/hf_py_code/compile/codes/results/"
  textseg_data: [int] = []
  inst_data: [int] = []
  with open(PREFIX+lang+"/text_segments.csv", mode='r', newline='') as file:
    for x in csv.DictReader(file):
      textseg_data.append(int(x["text_segment_size"]))
  with open(PREFIX+lang+"/instructions.csv", mode='r', newline='') as file:
    for x in csv.DictReader(file):
      inst_data.append(int(x["instructions"]))
  return textseg_data, inst_data

