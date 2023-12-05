from collections import deque
from rich import print

# Parsing
f = open('input.dat', 'r')
lines = f.readlines()
f.close()
seeds = [int(x) for x in lines[0].split(':')[1].strip().split(' ')]
i = -2
transitions = [[], [], [], [], [], [], []]
for line in lines:
    if line == '\n':
        continue
    if line[0].isalpha():
        i += 1
        continue
    transitions[i].append([int(x) for x in line.split()])

# Helper function
def overlap(l1, r1, l2, r2):
    a, i = max(l1, l2), min(r1, r2)
    if a <= i:
        return a, i
    else:
        return None

# Generating q
best = float('inf')
q = deque()
for i in range(0, len(seeds), 2):
    q.append((seeds[i], seeds[i]+seeds[i+1], 0))

# Iterate
while q:
    rstart, rend, map = q.popleft()
    if map == len(transitions):
        best = min(best, rstart)
        continue
    for dest, source, rng in transitions[map]:
        new = overlap(rstart, rend, source, source + rng)
        if new is None: continue
        q.append((new[0]-source+dest,new[1]-source+dest,map+1))

print(best)