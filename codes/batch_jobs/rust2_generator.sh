#!/bin/bash
start=209642
end=274641
TYPE=rust2
PREFIX="/lustre/schandra_crpl/users/3302/ir_bc_files/"
batch_size=200
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

    #for (( j=i; j<i+batch_size && j<=$end; j++ ))
    echo "for (( j=${i}; j<${i}+${batch_size} && j<=${end}; j++ ))" \
    >> ${js}
    echo "do" >> ${js}
        echo "/usr/bin/time -o \
        ${PREFIX}${TYPE}_time/time\${j}.txt \
        clang -O3 -c -o ${PREFIX}${TYPE}_out/file\${j}.o \
        ${PREFIX}${TYPE}/file\${j}.bc" >> ${js}
    echo "done" >> ${js}

    while true; do
        sbatch ${js} >> job_numbers.txt
        if [ $? -ne 0 ]; then
            #squeue -u andrewka --states=PD --noheader | wc -l
            echo "sbatch failed. Sleeping for 1 second..."
            sleep 1
        else
            break
        fi
    done
    rm ${js}
done

