from rich import print
import sys
# Input
grid = 0
with open('input.dat', 'r') as f:
    grid = [[c for c in x[:-1]] for x in f.readlines()]
m,n = len(grid), len(grid[0])
# Get start and end values
start = (0, grid[0].index('.'))
goal = (n-1, grid[-1].index('.'))
# Direction vectors
slopes = ['>', '<', '^', 'v'] 
dx = [0,0,-1,1]
dy = [1,-1,0,0]
# Function to determine next steps
def moves(i,j):
    # Standing on slope, must move in direction of slope
    if grid[i][j] in slopes:
        dir = slopes.index(grid[i][j])
        #print(f'We got {grid[i][j]} heading in ({dx[dir],dy[dir]})')
        ret = (i+dx[dir], j+dy[dir])
        if ret[0] in range(m) and ret[1] in range(n) and grid[ret[0]][ret[1]] != '#':
            return [ret]
        else:
            return []
    # Not standing on slope, move in all directions
    ret = []
    for z in range(4):
        new_pt = (i+dx[z], j+dy[z])
        if new_pt[0] in range(m) and new_pt[1] in range(n) and grid[new_pt[0]][new_pt[1]] != '#':
            ret.append(new_pt)
    return ret
# dfs
visited = [[False for _ in range(n)] for _ in range(m)]
def dfs(i: int, j: int, step: int):
    if (i,j) == goal:
        return step
    visited[i][j] = True
    best = 0
    for a,b in moves(i,j):
        if not visited[a][b]:
            score = dfs(a,b,step+1)
            best = max(best, score)
    visited[i][j] = False
    return best
# run dfs
sys.setrecursionlimit(99999999)
print(dfs(start[0],start[1],0))