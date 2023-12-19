from shapely.geometry import Polygon
from rich import print
# grab input
lines = 0
with open('input.dat', 'r') as f:
    lines = [x[:-1] for x in f.readlines()]
# define directions and points
directions = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
dirs = ['R','D','L','U']
i,j = 0,0
points = [(0,0)]
# Get a list of all the points
for line in lines:
    code = line.split(' ')[2][2:-1]
    direction = directions[dirs[int(code[-1])]]
    steps = int(code[:-1],base=16)
    i += direction[0] * steps
    j += direction[1] * steps
    points.append((i,j))
# Create a polygon for our dug out area
shape = Polygon(points)
print(shape.area + shape.length//2 + 1)