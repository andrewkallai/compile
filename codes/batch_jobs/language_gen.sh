#!/bin/bash

lang=("c" "cpp" "julia" "rust1" "rust2" "rust3" "rust4" "swift")
array1=(1 31654 87226 144642 209642 274642 339642 353701)
array2=(31653 87225 144641 209641 274641 339641 353700 402751)

length=${#lang[@]}

for (( i=0; i<$length; i++ ))
do
     > ${lang[$i]}_generator.sh
    echo "#!/bin/bash" >> ${lang[$i]}_generator.sh
    echo "start=${array1[$i]}" >> ${lang[$i]}_generator.sh
    echo "end=${array2[$i]}" >> ${lang[$i]}_generator.sh
    echo "TYPE=${lang[$i]}" >> ${lang[$i]}_generator.sh
    cat gen_template.sh >> ${lang[$i]}_generator.sh
    chmod 744 ${lang[$i]}_generator.sh 
done
