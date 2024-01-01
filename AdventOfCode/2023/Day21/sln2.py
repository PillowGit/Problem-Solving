from collections import deque
from numpy import polyfit
from rich import print
# Gather input
grid = 0
with open('input.dat', 'r') as f:
    grid = [[c for c in x[:-1]] for x in f.readlines()]
m,n = len(grid), len(grid[0])
grid[65][65] = '.'
# Function to generate valid moves from a position
def moves(i,j):
    ret = []
    for a,b in [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]:
        if grid[a%m][b%n] == '.':
            ret.append((a,b))
    return ret
# Function to determine # of valid stopping points given target steps
def run(max_step):
    endings = set()
    visited = set()
    q = deque()
    q.append((65,65,0))
    visited.add((65,65))
    while q:
        i,j,step = q.popleft()
        if step % 2 == max_step % 2:
            endings.add((i,j))
        if step == max_step:
            endings.add((i,j))
            continue
        for a,b in moves(i,j):
            if (a,b) not in visited:
                visited.add((a,b))
                q.append((a,b,step+1))
    return len(endings)
# Gather first 3 points for a polynomial fit
x,y = [],[]
for i in range(3):
    x.append(i)
    y.append(run(65+131*i))
res = [round(x) for x in polyfit(x,y,2,2e-100)]
print(res[0]*(202300**2)+res[1]*202300+res[2])