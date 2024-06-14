#!/bin/bash
PREFIX=/lustre/schandra_crpl/users/3302/ir_bc_files/

dirs=("c_result" "cpp_result" "julia_result" "rust1_result" "rust2_result" "rust3_result" "rust4_result" "swift_result" "c_out" "cpp_out" "julia_out" "rust1_out" "rust2_out" "rust3_out" "rust4_out" "swift_out")

for dir in "${dirs[@]}"; do
    rm -r ${PREFIX}${dir}/
    mkdir ${PREFIX}${dir}/
done

#rm ${PREFIX}c_result/*
#rm -r ${PREFIX}c_result/
#mkdir ${PREFIX}c_result/
#rm -r ${PREFIX}cpp_result/
#mkdir ${PREFIX}cpp_result/
#rm -r ${PREFIX}julia_result/
#mkdir ${PREFIX}julia_result/
#rm -r ${PREFIX}rust1_result/
#mkdir ${PREFIX}rust1_result/
#rm -r ${PREFIX}rust2_result/
#mkdir ${PREFIX}rust2_result/
#rm -r ${PREFIX}rust3_result/
#mkdir ${PREFIX}rust3_result/
#rm -r ${PREFIX}rust4_result/
#mkdir ${PREFIX}rust4_result/
#rm -r ${PREFIX}swift_result/
#mkdir ${PREFIX}swift_result/


