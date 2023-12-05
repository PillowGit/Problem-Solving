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

def solve(l, r, lvl):
    if lvl == len(transitions): return l
    scores = []
    for dest, source, width in transitions[lvl]:
        left = max(l, source)
        right = min(r, source+width)
        if left > right: continue
        scores.append(solve(left-source+dest, right-source+dest, lvl + 1))
    return min(scores) if scores else float('inf')

print(min([solve(seeds[i], seeds[i]+seeds[i+1], 0) for i in range(0, len(seeds), 2)]))