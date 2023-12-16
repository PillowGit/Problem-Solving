from rich import print

lines = 0
with open('input.dat', 'r') as f:
    lines = [x[:-1] for x in f.readlines()]

# Hash functions
mod = 256
def hash(key: str) -> int:
    res = 0
    for x in key:
        res = (res+ord(x))*17
        res %= mod
    return res

# Hashmap Functions
map = {x:[] for x in range(256)}
def remove(key):
    hashed = hash(key)
    found = -1
    for i in range(len(map[hashed])):
        if map[hashed][i][0] == key:
            found = i
            break
    if found != -1:
        map[hashed].pop(found)
def add(key,val):
    hashed = hash(key)
    found = -1
    for i in range(len(map[hashed])):
        if map[hashed][i][0] == key:
            found = i
            break
    if found == -1:
        map[hashed].append([key, val])
    else:
        map[hashed][found][1] = val

# Build boxes
inp = ''.join(lines)
for code in inp.split(','):
    if '=' in code:
        print(code)
        k, v = code.split('=')
        add(k, int(v))
    else:
        remove(code[:-1])

# Calculate answer
print(map)
ans = 0
for i, box in enumerate(map.values()):
    for j, dat in enumerate(box):
        ans += (i+1) * (j+1) * dat[1]
print(ans)