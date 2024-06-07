#!/bin/bash
start=1
end=2

for (( i=$start; i<=$end; i++ ))
do
    cp template.qs example_$i.sh
    #cat example_$i.sh
    #rm -iv example_$i.sh
    #echo "echoMe $i" >> example_$i.sh
    #clang -O3 -c -o 3file.out file3.bc
    #sbatch example_${i}.sh
done
