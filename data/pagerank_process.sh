#!/bin/bash
i=0
n_iterations=5
input=input.txt
python_ver=python2.7 # Change this to however you invoke python

while [ $i -lt $n_iterations ]
do
    $python_ver pagerank_map.py < $input |
    sort |
    $python_ver pagerank_reduce.py |
    $python_ver process_map.py |
    sort |
    $python_ver process_reduce.py > output.txt

    read -r line < output.txt # reads first line of output.txt
    first_nine=${line:0:9}    # FinalRank is 9 characters

    if [ "$first_nine" = "FinalRank" ] # Converged
    then
        echo "Converged!"
        break
    else
        echo "Try again"
        input=output.txt  # Pipe output to pagerank_map
    fi

    ((i++))
done
