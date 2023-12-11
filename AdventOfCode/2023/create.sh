#!/bin/bash

echo "Which AoC Day is it?"

read daynum

if [ ! -d "./Day$daynum" ]; then
	year=$(basename "$PWD")
	mkdir "Day$daynum"
	cd "Day$daynum"
	touch input.dat
	touch sln1.py
	touch sln2.py
	aocd $daynum $year > input.dat
else
	echo "A folder for Day $daynum already exists"
fi
