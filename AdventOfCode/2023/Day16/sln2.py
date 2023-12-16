from collections import deque
from rich import print

grid = 0
with open('input.dat', 'r') as f:
    grid = [[c for c in x[:-1]] for x in f.readlines()]
m, n = len(grid), len(grid[0])


def laser(a, b, d):
    q = deque()
    q.append((a,b,d))
    energized = set()
    seen = set()
    def simulate():
        i, j, direction = q.popleft()
        if i not in range(m) or j not in range(n) or (i,j,direction) in seen:
            return None
        else:
            seen.add((i, j, direction))
        energized.add((i,j))
        tile = grid[i][j]
        if direction == 'r':
            if tile in '.-':
                q.append((i, j+1, direction))
            elif tile == '\\':
                q.append((i+1,j,'d'))
            elif tile == '/':
                q.append((i-1,j,'u'))
            elif tile == '|':
                q.append((i+1,j,'d'))
                q.append((i-1,j,'u'))
        if direction == 'l':
            if tile in '.-':
                q.append((i, j-1, direction))
            elif tile == '\\':
                q.append((i-1,j,'u'))
            elif tile == '/':
                q.append((i+1,j,'d'))
            elif tile == '|':
                q.append((i+1,j,'d'))
                q.append((i-1,j,'u'))
        if direction == 'u':
            if tile in '.|':
                q.append((i-1, j, direction))
            elif tile == '\\':
                q.append((i,j-1,'l'))
            elif tile == '/':
                q.append((i,j+1,'r'))
            elif tile == '-':
                q.append((i,j-1,'l'))
                q.append((i,j+1,'r'))
        if direction == 'd':
            if tile in '.|':
                q.append((i+1, j, direction))
            elif tile == '\\':
                q.append((i,j+1,'r'))
            elif tile == '/':
                q.append((i,j-1,'l'))
            elif tile == '-':
                q.append((i,j-1,'l'))
                q.append((i,j+1,'r'))
    while q:
        simulate()
    return len(energized)

scores = []
for i in range(m):
    scores.append(laser(i, 0, 'r'))
    scores.append(laser(i,n-1,'l'))
for j in range(n):
    scores.append(laser(0,j,'d'))
    scores.append(laser(m-1,j,'u'))
print(max(scores))