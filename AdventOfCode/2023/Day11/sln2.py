from rich import print

lines = [x[:-1] for x in open('input.dat', 'r').readlines()]

rows=[]

for i in range(len(lines)):
    if "#" not in lines[i]:
        rows.append(i)


cols=[]
for r in range(len(lines[0])):
    for i in range(len(lines)):
        if lines[i][r]=="#":break
    else:
        cols.append(r)


print(rows)
print(cols)
galaxies=set()

ii=0
rr=0
for i in range(len(lines)):
    if i in rows:
        ii+=1000000
        ii-=1
    rr=0
    for r in range(len(lines[0])):
        if r in cols:
            rr+=1000000
            rr-=1
        if lines[i][r]=="#":
            galaxies.add((i+ii,r+rr))

galaxies=list(galaxies)
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