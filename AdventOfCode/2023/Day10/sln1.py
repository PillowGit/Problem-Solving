from collections import deque

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
ans = 0
q = deque()
# S is -
q.append((start[0], start[1], 'l', 0))
q.append((start[0], start[1], 'r', 0))
while q:
    i, j, direction, step = q.popleft()
    if type(grid[i][j]) == int: continue
    ans = max(ans, step)
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
    print(f'Moving from {grid[i][j]} to {grid[x][y]} with instruction {move}')
    if  i != start[0] and j != start[1]:
        grid[i][j] = step
    q.append((x, y, move, step+1))
print(ans)