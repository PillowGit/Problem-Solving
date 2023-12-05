from collections import deque
from rich import print

f = open('input.dat', 'r')
lines = f.readlines()
f.close()

seeds = [int(x) for x in lines[0].split(':')[1].strip().split(' ')]
lines.pop(0)
lines.pop(0)

i = 0
sts = []
stf = []
ftw = []
wtl = []
ltt = []
tth = []
htl = []
for line in lines:
    if line == '\n':
        continue
    if line[0].isalpha():
        i += 1
        continue
    
    dat = [int(x) for x in line.split()]
    match i:
        case 1:
            sts.append(dat)
        case 2:
            stf.append(dat)
        case 3:
            ftw.append(dat)
        case 4:
            wtl.append(dat)
        case 5:
            ltt.append(dat)
        case 6:
            tth.append(dat)
        case 7:
            htl.append(dat)

ops = [sts, stf, ftw, wtl, ltt, tth, htl]
best = float('inf')
q = deque([(s, 0) for s in seeds])
while q:
    curr, map = q.popleft()
    if map == len(ops):
        best = min(best, curr)
        continue
    for dest, source, rng in ops[map]:
        if curr in range(source, source+rng):
            offset = curr - source
            q.append((offset+dest, map+1))

print(best)

"""
Wrong:
297680497
"""