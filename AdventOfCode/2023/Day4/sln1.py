f = open('input.dat', 'r')
lines = [x[:-1] for x in f.readlines()]
f.close()

ans = 0

print(sum((lambda z:0 if z == 0 else 2**(z-1))((lambda a,b:len(set(a).intersection(b)))(*[x.strip().replace('  ',' ').split(' ') for x in line[:-1].split(':')[1].split('|')])) for line in open('input.dat','r').readlines()))
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


print(f'{ans} and {ol}')
