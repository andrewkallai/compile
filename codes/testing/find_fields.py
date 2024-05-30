#!/usr/bin/env python3
# -*- coding: ascii -*-
# find_fields.py
from datasets import load_dataset

ds = load_dataset('llvm-ml/ComPile', split='train')
start_index = -1;
DATA_LEN = len(ds);
current_value = "";

#i=0
#while(1):
#  if (ds[i]["language"] != "c"):
#    print(i, ds[i]["language"])
#    break;
#  i+=1;

#for i in range(0, DATA_LEN):
# current_value = ds[i]["language"] 
# if ((current_value != "cpp") and (start_index != -1)):
#   print(start_index, i-1)
#   start_index = -1;
#   print(ds[i]["language"])
#   break;
# elif ((current_value == "cpp") and (start_index == -1)):
#   start_index = i;

 
for i in range(0, DATA_LEN):
 current_value = ds[i]["language"] 
 if ((current_value != "cpp") and (start_index != -1)):
   print(start_index, i-1)
   start_index = -1;
 elif ((current_value == "cpp") and (start_index == -1)):
   start_index = i;
    
