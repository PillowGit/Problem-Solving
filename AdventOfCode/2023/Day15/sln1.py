from rich import print

lines = 0
with open('input.dat', 'r') as f:
    lines = [x[:-1] for x in f.readlines()]

mod = 256
def hash(key: str) -> int:
    res = 0
    for x in key:
        res = (res+ord(x))*17
        res %= mod
    return res

inp = ''.join(lines)
print(inp)
ans = 0
for code in inp.split(','):
    ans += hash(code)
print(ans)