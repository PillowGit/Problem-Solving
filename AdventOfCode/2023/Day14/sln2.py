from aocutil import graph
from rich import print

lines = 0
with open('input.dat', 'r') as f:
    lines = [x[:-1] for x in f.readlines()]

graph.hey()