from rich import print
import sympy
# input
lines = 0
with open('input.dat', 'r') as f:
    lines = [x[:-1] for x in f.readlines()]
n = len(lines)
# parse
pts = []
dirs = []
for i in range(3):
    line = lines[i]
    p, d = [x.split(',') for x in line.replace(' ','').split('@')]
    p, d = tuple([int(x) for x in p]), tuple([int(x) for x in d])
    pts.append(p), dirs.append(d)
# Make symbols for sympy to use
x, y, z, dx, dy, dz, t1, t2, t3 = sympy.symbols('x y z dx dy dz t1 t2 t3', real=True)
# Pack them into equations
equations = [
    sympy.Eq(x + dx * t1, pts[0][0] + dirs[0][0] * t1),
    sympy.Eq(y + dy * t1, pts[0][1] + dirs[0][1] * t1),
    sympy.Eq(z + dz * t1, pts[0][2] + dirs[0][2] * t1),
    sympy.Eq(x + dx * t2, pts[1][0] + dirs[1][0] * t2),
    sympy.Eq(y + dy * t2, pts[1][1] + dirs[1][1] * t2),
    sympy.Eq(z + dz * t2, pts[1][2] + dirs[1][2] * t2),
    sympy.Eq(x + dx * t3, pts[2][0] + dirs[2][0] * t3),
    sympy.Eq(y + dy * t3, pts[2][1] + dirs[2][1] * t3),
    sympy.Eq(z + dz * t3, pts[2][2] + dirs[2][2] * t3)
]
# Sympy my beloved
ans = sympy.solve(equations)[0]
# print ans
print(ans[x] + ans[y] + ans[z])