f = open('input.dat', 'r')
lines = [x[:-1] for x in f.readlines()]
f.close()

ans = 0

for line in lines:
    w, u = line.split(':')[1].split('|')
    w = w.strip()
    u = u.strip()
    w = w.replace('  ', ' ')
    u = u.replace('  ', ' ')
    w = w.split(' ')
    u = u.split(' ')
    matches = set(w).intersection(set(u))
    i = len(matches)
    res = 0
    if i:
        res = 1
        i -= 1
    for _ in range(i):
        res *= 2 
    ans += res

print(ans)
