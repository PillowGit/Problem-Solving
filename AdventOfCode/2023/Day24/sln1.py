from itertools import combinations
from rich import print
# input
lines = 0
with open('input.dat', 'r') as f:
    lines = [x[:-1] for x in f.readlines()]
n = len(lines)
# parse
pts = []
dirs = []
for line in lines:
    p, d = [x.split(',') for x in line.replace(' ','').split('@')]
    p, d = tuple([int(x) for x in p][:-1]), tuple([int(x) for x in d][:-1])
    pts.append(p), dirs.append(d)
# Function to determine if two points collide
def collides(l: int, r: int):
    x1, y1 = pts[l]
    dx1, dy1 =  dirs[l]
    x2, y2 = pts[r]
    dx2, dy2 = dirs[r]
    if dx1 * dy2 - dy1 * dx2 == 0: return dx1 * (y1-y2) + dy1 * (x2-x1) == 0
    t2 = (dx1 * (y1 - y2) + dy1 * (x2 - x1) ) / (dx1 * dy2 - dy1 * dx2)
    t1 = (x2 - x1 + dx2 * t2) / dx1
    if t1 < 0 or t2 < 0: return False
    x,y = x2 + dx2 * t2, y2 + dy2 * t2
    l, r = 200000000000000, 400000000000000
    return l <= x <= r and l <= y <= r
# Find ans
ans = 0
for i,j in combinations(list(range(n)),2):
    if collides(i,j): ans += 1
print(ans)
"""
Wrong:
20442 - high
"""