#!/bin/bash

word="phrase"
shading_chars=( '░' '▒' '▓' '█' )

for (( i=0; i<${#word}; i++ )); do
    idx=$((i % ${#shading_chars[@]}))
    echo -n "${shading_chars[$idx]}${word:$i:1}"
done

echo
