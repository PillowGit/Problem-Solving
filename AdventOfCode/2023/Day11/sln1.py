from rich import print

lines = [x[:-1] for x in open('input.dat', 'r').readlines()]

# Expand rows
pic = []
for row in lines:
    pic.append(row)
    if '#' not in row:
        pic.append(row)

# Transpose
pic = list(zip(*pic))
expanded = []
expanded[::] = pic
pic = []

# Columns now
for col in expanded:
    pic.append(col)
    if '#' not in col:
        pic.append(col)

# Find galaxies
galaxies = []
for r in range(len(pic)):
    for c in range(len(pic[r])):
        if pic[r][c] == '#':
            galaxies.append((r, c))

ans = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        x1, y1 = galaxies[i]
        x2, y2 = galaxies[j]
        ans += abs(x1-x2) + abs(y1-y2)
print(ans)

"""
Wrong:
9361767
"""