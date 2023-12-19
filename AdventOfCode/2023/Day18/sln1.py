from collections import deque
from rich import print

lines = 0
with open('sample.dat', 'r') as f:
    lines = [x[:-1] for x in f.readlines()]
directions = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
dirs = ['R','D','L','U']
# Construct our grid
i, j = 0, 0
l, r, u, d = 0,0,0,0
for line in lines:
    direction, steps, color = line.split(' ')
    direction = directions[direction]
    steps = int(steps)
    color = color.replace('(','').replace(')','')
    for _ in range(steps):
        i += direction[0]
        j += direction[1]
    l = min(l, j)
    r = max(r, j)
    u = min(u, i)
    d = max(d, i)
grid = [['.' for _ in range(r-l+1)] for _ in range(d-u+1)]
# Create digging path outline
i,j = (-1)*u,(-1)*l
grid[i][j] = '#'
for line in lines:
    direction, steps, color = line.split(' ')
    direction = directions[direction]
    steps = int(steps)
    color = color.replace('(','').replace(')','')
    for _ in range(steps):
        i += direction[0]
        j += direction[1]
        grid[i][j] = '#'
# Show grid
def show_grid():
    print('\n'.join(''.join(c for c in line) for line in grid))
# Find start pos
i,j = 0,0
c = 1
while i < len(grid):
    if c == 0 and grid[i][j] == '#':
        j += 1
        break
    elif grid[i][j] == '#':
        c -= 1
    i += 1
# bfs to fill out the shit
q = deque()
q.append((i,j))
seen = set()
seen.add((i,j))
while q:
    curr = q.popleft()
    for d in directions.values():
        new = (curr[0] + d[0], curr[1] + d[1])
        if new not in seen and grid[new[0]][new[1]] != '#':
            seen.add(new)
            q.append(new)
# end
print(len(seen)+''.join(''.join(c for c in line) for line in grid).count('#'))
"""
wrong:
63445 # didnt include dug holes in simulation
"""