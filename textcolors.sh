#!/bin/bash

# Function to colorize text
colorize_text() {
    color_code=$1
    text=$2
    echo -e "\e[38;5;${color_code}m${text}\e[0m"
}

# User input for the word to display
read -p "Enter a word to display: " word

# Define an array of shading characters and colors
shading_chars=( '░' '▒' '▓' '█' )
colors=( 39 196 202 208 214 220 226 )

# Loop through the word and apply shading and colors
for (( i=0; i<${#word}; i++ )); do
    shading_idx=$((i % ${#shading_chars[@]}))
    color_idx=$((i % ${#colors[@]}))
    shaded_text="${shading_chars[$shading_idx]}${word:$i:1}"
    colorize_text ${colors[$color_idx]} "$shaded_text"
done