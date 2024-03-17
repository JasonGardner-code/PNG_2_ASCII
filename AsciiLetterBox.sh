#!/bin/bash

# Function to display ASCII art for a single letter with box
display_boxed_letter() {
    local letter=$1
    echo "##########"
    echo "#        #"
    echo "#   $letter   #"
    echo "#        #"
    echo "##########"
}

# Convert input text to uppercase
input=$(echo $1 | tr '[:lower:]' '[:upper:]')

# Loop through each character in the input text
for (( i=0; i<${#input}; i++ )); do
    letter=${input:$i:1}
    if [[ $letter =~ [A-Z] ]]; then
        display_boxed_letter $letter
    else
        echo "Invalid character: $letter"
    fi
done
