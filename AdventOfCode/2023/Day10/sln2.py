from collections import deque
from rich import print

f = open('input.dat', 'r')
lines = [x[:-1] for x in f.readlines()]
f.close()

# Make grid
grid = [[c for c in line] for line in lines]

# Find S
start = 0
for i, row in enumerate(grid):
    if 'S' in row:
        start = (i,row.index('S'))
        break

# Traverse
q = deque()
# S is -
main = set()
q.append((start[0], start[1], 'l'))
q.append((start[0], start[1], 'r'))
while q:
    i, j, direction = q.popleft()
    if (i,j) in main and (i,j) != start: continue
    else: main.add((i,j))
    x, y = i, j
    if direction == 'l':
        y -= 1
    elif direction == 'r':
        y += 1
    elif direction == 'u':
        x -= 1
    else:
        x += 1
    pipe = grid[x][y] 
    move = ''
    if pipe == 'L':
        if direction == 'd':
            move = 'r'
        else:
            move = 'u'
    elif pipe == 'J':
        if direction == 'd':
            move = 'l'
        else:
            move = 'u'
    elif pipe == '7':
        if direction == 'r':
            move = 'd'
        else:
            move = 'l'
    elif pipe == 'F':
        if direction == 'u':
            move = 'r'
        else:
            move = 'd'
    else:        
        move = direction
    q.append((x, y, move))

# Find north facing pipes within main loop
ans = 0
north_facing = '|JL'
for i in range(len(grid)):
    pipes = 0
    for j in range(len(grid[0])):
        if (i,j) in main:
            if grid[i][j] in north_facing:
                pipes += 1
            continue
        else:
            if pipes % 2 == 1:
                ans += 1
                continue
print(ans)

"""
wrong:
306
311
298
right:
433
"""