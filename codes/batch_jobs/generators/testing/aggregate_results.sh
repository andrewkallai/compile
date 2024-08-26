#!/bin/bash

# Initialize an associative array to store the total counts for each field
declare -A totals

# Function to process the analysis of a function and update the totals
process_function_analysis() {
    while read -r line; do
        # Ignore lines that don't contain key-value pairs
        if [[ $line == *:* ]]; then
            key=$(echo "$line" | cut -d':' -f1 | xargs)
            value=$(echo "$line" | cut -d':' -f2 | xargs)
            totals[$key]=$((totals[$key] + value))
        fi
    done
}

# Read input and process each function analysis block
while IFS= read -r line; do
    if [[ $line == Printing* ]]; then
        continue
    elif [[ -z $line ]]; then
        continue
    else
        echo "$line" | process_function_analysis
    fi
done

# Print the aggregated results
echo "Aggregated CFA Analysis Results:"
for key in "${!totals[@]}"; do
    echo "$key: ${totals[$key]}"
done

