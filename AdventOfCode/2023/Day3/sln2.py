f = open('input.dat','r')
lines = [x[:-1] for x in f.readlines()]
f.close()

ans = 0
lines = [[c for c in x] for x in lines]

def read(r, c):
    n = ''
    while c >= 0 and lines[r][c].isdigit():
        c -= 1
    c += 1
    while c < len(lines[0]) and lines[r][c].isdigit(): 
        n += lines[r][c]
        c += 1
    return int(n)

def find_adj(x, y):
    global ans
    adj = set()
    for a, b in [[x, y-1], [x-1,y-1], [x-1, y], [x-1, y+1], [x, y+1], [x+1, y+1], [x+1, y] ,[x+1, y-1]]:
        if a in range(140) and b in range(140) and lines[a][b].isdigit():
            adj.add(read(a, b))
    if len(adj) == 2:
        l = list(adj)
        ans += l[0] * l[1]

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == '*':
            find_adj(i, j)

print(ans)

"""
Wrong Answers:
8803835
342942
323258
"""