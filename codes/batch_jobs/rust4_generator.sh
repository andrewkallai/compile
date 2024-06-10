#!/bin/bash
start=339642
end=353700
PREFIX="/lustre/schandra_crpl/users/3302/ir_bc_files/"
TYPE="rust4"

echo "${TYPE}" >> job_numbers.txt
date >> job_numbers.txt
for (( i=$start; i<=$end; i++ ))
do
    cp template1.qs p_$i.sh
    echo "#SBATCH \
    --output=${PREFIX}${TYPE}_result/${i}-%j.out" \
    >> p_${i}.sh
    echo "#SBATCH \
    --error=${PREFIX}${TYPE}_result/${i}-%j.out" \
    >> p_${i}.sh
    cat template2.qs >> p_$i.sh
    echo "clang -O3 -c -o \
    ${PREFIX}${TYPE}_out/file${i}.o ${PREFIX}${TYPE}/file${i}.bc" \
    >> p_${i}.sh
    echo "rm p_${i}.sh" >> p_${i}.sh
    #cat p_$i.sh
    sbatch p_${i}.sh >> job_numbers.txt
done
