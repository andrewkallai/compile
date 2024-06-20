#!/bin/bash

PREFIX="/lustre/schandra_crpl/users/3302/ir_bc_files/"
n=31653

for ((i=1; i<=n; i++)); do

#  awk -F, '{print $2}' "${PREFIX}/c_textseg/textseg${i}.csv" >> "text_segments.csv"
  awk -F, '{print $2}' "${PREFIX}c_inst/inst${i}.csv" >> "instructions.csv"
done

