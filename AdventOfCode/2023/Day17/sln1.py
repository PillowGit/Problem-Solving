from rich import print
from heapq import *

grid = 0
with open('input.dat', 'r') as f:
    grid = [[int(c) for c in x[:-1]] for x in f.readlines()]
m, n = len(grid), len(grid[0])

directions = [(0,1), (1,0), (0,-1), (-1,0)]

q = [(0,0,0,-1)] # cost, x, y, direction
ans = 0
seen = set()
costs = {}
while q:
    c, x, y, d = heappop(q)
    # at answer
    if x == m-1 and y == n-1:
        ans = c
        break
    # already seen
    if (x,y,d) in seen:
        continue
    else:
        seen.add((x,y,d))
    # moves (0-3 for r,u,l,d)
    for direction in range(4):
        increase = 0
        # crucible limit, 3 moves max
        if direction == d or (direction+2)%4 == d:
            continue
        # move all lengths at once
        for dist in range(1, 4):
            i = x + directions[direction][0] * dist
            j = y + directions[direction][1] * dist
            # if in range
            if i in range(m) and j in range(n):
                # calculate amnt
                increase += grid[i][j]
                new_cost = c + increase
                # if in seen and not the best path to get here then leave
                if (i,j,direction) in costs and costs[(i,j,direction)] <= new_cost:
                    continue
                # push to seen and add to q
                costs[(i,j,direction)] = new_cost
                heappush(q, (new_cost, i, j, direction))
print(ans)