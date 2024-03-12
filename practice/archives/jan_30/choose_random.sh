#!/bin/bash

# Store each line of stdin in an array
mapfile -t lines

# Get the number of lines
num_lines=${#lines[@]}

# Select a random index within the range of lines
random_index=$(( RANDOM % num_lines ))

# Output the randomly selected line
echo "${lines[random_index]}"

