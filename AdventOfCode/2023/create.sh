#!/bin/bash

echo "Which AoC Day is it?"

read daynum

if [ ! -d "./Day$daynum" ]; then
	year=$(basename "$PWD")

	cp -R "./template" "./Day$daynum"

	cd "Day$daynum"
	aocd $daynum $year > input.dat
else
	echo "A folder for Day $daynum already exists"
fi
