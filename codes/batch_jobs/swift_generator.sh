#!/bin/bash
start=353701
end=402751
TYPE=swift
PREFIX="/lustre/schandra_crpl/users/3302/ir_bc_files/"
batch_size=100
echo "${TYPE}" >> job_numbers.txt
date >> job_numbers.txt

for (( i=$start; i<=$end; i+=$batch_size ))
do
    js="p_${i}.sh"
    cp template1.sh $js
    echo "#SBATCH \
    --output=${PREFIX}${TYPE}_result/${i}-%j.out" >> $js
    echo "#SBATCH \
    --error=${PREFIX}${TYPE}_result/${i}-%j.out" >> $js
    cat template2.sh >> $js

    STOP=$((i+batch_size-1))
    if [ $STOP -gt ${end} ]; then
      STOP=${end} 
    fi
    echo "cd ${PREFIX}" >> ${js}
    echo "make --always-make -i -f ./makefile -j 64 \
    lang="${TYPE}" begin="${i}" \
    end="${STOP}"" >> ${js}

    while true; do
        sbatch ${js} >> job_numbers.txt
        if [ $? -ne 0 ]; then
            squeue -u andrewka --states=PD --noheader | wc -l
            echo "sbatch failed. Sleeping for 1 second..."
            sleep 1
        else
            break
        fi
    done
    rm ${js}
done

