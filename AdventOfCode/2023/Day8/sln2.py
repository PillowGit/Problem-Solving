from rich import print
from math import lcm

f = open('input.dat', 'r')
lines = [x[:-1] for x in f.readlines()]
f.close()

instructions = lines[0]
directions = {}
way = lambda z:1 if z == 'R' else 0
starts = []
for line in lines[2:]:
    f, t = line.split('=')
    f=f.strip()
    t=t.strip()
    t=t.replace('(','')
    t=t.replace(')','')
    t=t.replace(',','')
    t=t.split(' ')
    directions[f] = t
    if f[2] == 'A':
        starts.append(f)

ends = []
for path in starts:
    i = 0
    cur = path
    while cur[2] != 'Z':
        cur = directions[cur][way(instructions[i%len(instructions)])]
        i += 1
    ends.append(i)
print(lcm(*ends))