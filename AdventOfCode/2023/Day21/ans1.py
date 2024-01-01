from collections import deque
from rich import print
# Gather input
grid = 0
with open('input2.dat', 'r') as f:
    grid = [[c for c in x[:-1]] for x in f.readlines()]
m,n = len(grid), len(grid[0])
grid[65][65] = '.'
# Helper functions
def moves(i,j):
    ret = []
    for a,b in [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]:
        if grid[a%m][b%n] == '.':
            ret.append((a,b))
    return ret
def run(max_step):
    # bfs
    endings = set()
    visited = set()
    # Find starting point
    q = deque() # format is [(i, j, step)]
    q.append((65,65,0))
    visited.add((65,65))
    while q:
        i,j,step = q.popleft()
        if step % 2 == max_step%2:
            endings.add((i,j))
        if step == max_step:
            endings.add((i,j))
            continue
        for a,b in moves(i,j):
            if (a,b) not in visited:
                visited.add((a,b))
                q.append((a,b,step+1))
    return len(endings)
"""
65 3884 3884 0
196 34564 30680 1
327 95816 61252 2
3884
34564
95816
"""