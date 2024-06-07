input=("bill" "ted" "lisa" "42")
for i in ${input[*]}
do
    cp example.sh example_${i}.sh
    echo "echoMe $i" >> example_${i}.sh
    sbatch example_${i}.sh
done
