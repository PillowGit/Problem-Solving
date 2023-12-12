#!/bin/bash

if [ "$#" -eq 1 ]; then
	if [ ! -d "./Day$1" ]; then
		year=$(basename "$PWD")

		cp -R "./template" "./Day$1"

		cd "Day$1"
		aocd $1 $year > input.dat
	else
		echo "A folder for day $1 already exists"
	fi
else
    echo "Please provide the day to clone when running the script"
fi
