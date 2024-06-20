# -*- coding: ascii -*-
import csv

PREFIX: str = "/lustre/schandra_crpl/users/3302/ir_bc_files/"

textseg_data: [int] = []
inst_data: [int] = []
#for i in range(1,31654): 
for i in (num for num in range(1,31654) if num not in {24761}): 
  with open(PREFIX+"c_textseg/textseg"+str(i)+".csv", mode='r', newline='') as file:
    #print(type(value))
    for x in csv.reader(file):
      #print(x[1])
      #print(type(x[1]))
      textseg_data.append(int(x[1]))
  with open(PREFIX+"c_inst/inst"+str(i)+".csv", mode='r', newline='') as file:
    for x in csv.reader(file):
      inst_data.append(int(x[1]))

#print(data)

