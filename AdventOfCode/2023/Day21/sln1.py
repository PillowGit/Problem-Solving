from collections import deque
from rich import print
# Gather input
grid = 0
with open('input.dat', 'r') as f:
    grid = [[c for c in x[:-1]] for x in f.readlines()]
m,n = len(grid), len(grid[0])
# Helper functions
def moves(i,j):
    ret = []
    for a,b in [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]:
        if a in range(m) and b in range(n) and grid[a][b] == '.':
            ret.append((a,b))
    return ret
def grid_str():
    return '\n'.join(''.join(c for c in r) for r in grid)
# Find starting point
q = deque() # format is [(i, j, step)]
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'S':
            q.append((i,j,0))
grid[q[0][0]][q[0][1]] = '.'
# bfs
endings = set()
visited = set()
visited.add((q[0][0],q[0][1]))
while q:
    i,j,step = q.popleft()
    if step % 2 == 0:
        endings.add((i,j))
    if step == 64: continue
    for a,b in moves(i,j):
        if (a,b) not in visited:
            visited.add((a,b))
            q.append((a,b,step+1))
# debug
def debug():
    for i,j in list(endings):
        grid[i][j] = 'O'
    print(grid_str())
#debug()
# answer
print(len(endings))

"""
wrong
7689
3514
"""