from rich import print
import numpy as np
# input
lines = 0
with open('sample.dat', 'r') as f:
    lines = [x[:-1] for x in f.readlines()]
# parse
out = 'local pts = {\n'
for line in lines:
    out += '\t{' + line.replace(' ','').replace('@',',') + '},\n'
print(out[:-2]+'\n}')