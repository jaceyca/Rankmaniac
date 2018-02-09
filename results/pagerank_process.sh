#!/bin/bash
i=0
n_iterations=50
input=input.txt
python_ver=python # Change this to however you invoke python

while [ $i -lt $n_iterations ]
do
    $python_ver pagerank_map.py < $input |
    sort |
    $python_ver pagerank_reduce.py |
    $python_ver process_map.py |
    sort > input_to_process_reduce.txt
    $python_ver process_reduce.py < input_to_process_reduce.txt > output.txt

    read -r line < output.txt # reads first line of output.txt
    first_nine=${line:0:9}    # FinalRank is 9 characters

    if [ "$first_nine" = "FinalRank" ] # Converged
    then
        echo "Converged!"
        echo $i
        sleep 5
        break
    else
        echo "Try again"
        input=output.txt  # Pipe output to pagerank_map
    fi

    ((i++))
done
