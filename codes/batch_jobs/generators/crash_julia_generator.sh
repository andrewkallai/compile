#!/bin/bash
start=87226
end=144641
TYPE=julia
batch_size=145
PREFIX="/lustre/schandra_crpl/users/3302/ir_bc_files/"
cd /home/3302/hf_py_code/compile/codes/batch_jobs/generators
echo "${TYPE}" >> job_numbers.txt
date >> job_numbers.txt

for (( i=$start; i<=$end; i+=$batch_size ))
do
    js="p_${i}.sh"
    cp template1.sh $js
    echo "#SBATCH \
    --output=${PREFIX}${TYPE}/job_results/${i}-%j.out" >> $js
    echo "#SBATCH \
    --error=${PREFIX}${TYPE}/job_results/${i}-%j.out" >> $js
    cat template2.sh >> $js

    STOP=$((i+batch_size-1))
    if [ $STOP -gt ${end} ]; then
      STOP=${end} 
    fi
    echo "cd ${PREFIX}" >> ${js}
    echo "make -i -f ./julia_makefile -j 64 \
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

