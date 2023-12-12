#!/bin/bash

# Check if the script has been provided with exactly one argument
if [ "$#" -eq 1 ]; then
    clear
    python3 "sln$1.py"
else
    echo "Please provide exactly one argument for which file to run"
fi