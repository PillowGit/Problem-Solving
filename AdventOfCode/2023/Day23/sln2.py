from rich import print
import sys
#input
grid = 0
with open('input.dat', 'r') as f:
    grid = [[c for c in x[:-1]] for x in f.readlines()]
m,n = len(grid), len(grid[0])
# Get start and end values
start = (0, grid[0].index('.'))
goal = (n-1, grid[-1].index('.'))
# Direction vectors
dx = [0,0,-1,1]
dy = [1,-1,0,0]
# Function to determine next steps
def moves(i,j):
    # Not standing on slope, move in all directions
    ret = []
    for z in range(4):
        new_pt = (i+dx[z], j+dy[z])
        if new_pt[0] in range(m) and new_pt[1] in range(n) and grid[new_pt[0]][new_pt[1]] != '#':
            ret.append(new_pt)
    return ret
# dfs
ans = -1
visited = [[False for _ in range(n)] for _ in range(m)]
def dfs(i: int, j: int, step: int):
    global ans
    if (i,j) == goal:
        if step > ans:
            ans = step
            print(ans)
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