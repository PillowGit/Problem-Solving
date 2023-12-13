from rich import print

lines = 0
with open('input.dat', 'r') as f:
    lines = [x[:-1] for x in f.readlines()]
    
def cmp(l: str, r: str) -> int:
    diff = 0
    for i in range(len(l)):
        if l[i] != r[i]:
            diff += 1
    return diff

def solve(pattern: list[str]) -> int:
    n = len(pattern)
    res = (-1, -1)
    for i in range(1, n):
        l, r = i-1, i
        score = 0 
        smudges = 0
        while 0 <= l and r < n:
            smudges += cmp(pattern[l], pattern[r])
            if smudges > 1:
                score = -1
                break
            else:
                score += 1
                l -= 1
                r += 1
        if score > res[0] and smudges == 1:
            res = (score, i)
    ans =  res[1]*100 if res[0] != -1 else solve([''.join(s) for s in zip(*pattern)])//100
    return ans

cur, ans = [], 0
lines.append('')
for line in lines:
    if line == '':
        ans += solve(cur)
        cur = []
    else:
        cur.append(line)
print(ans)