#!/bin/bash

start=1
end=31653
batch_size=5000
PREFIX="/lustre/schandra_crpl/users/3302/ir_bc_files/"
TYPE="c"

echo "${TYPE}" >> job_numbers.txt
date >> job_numbers.txt

for (( i=$start; i<=$end; i+=$batch_size ))
do
    js="p_${i}.sh"
    cp template1.qs $js
    echo "#SBATCH \
    --output=${PREFIX}${TYPE}_result/${i}-%j.out" >> $js
    echo "#SBATCH \
    --error=${PREFIX}${TYPE}_result/${i}-%j.out" >> $js
    cat template2.qs >> $js

    for (( j=i; j<i+batch_size && j<=$end; j++ ))
    do
        echo "clang -O3 -c -o ${PREFIX}${TYPE}_out/file${j}.o \
        ${PREFIX}${TYPE}/file${j}.bc" >> ${js} 
    done

    while true; do
        sbatch ${js} >> job_numbers.txt
        if [ $? -ne 0 ]; then
            echo "sbatch failed. Sleeping for 1 second..."
            sleep 1
        else
            break
        fi
    done
    rm ${js}
done

