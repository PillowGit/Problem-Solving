from rich import print

f = open('input.dat', 'r')
lines = [x[:-1] for x in f.readlines()]
f.close()

ans = 0

copies = {}
for l in range(len(lines)):
    copies[l] = 1
for i, line in enumerate(lines):
    if copies[i] == 0:
        break
    ans += copies[i]

    w, u = line.split(':')[1].split('|')
    w = w.strip()
    u = u.strip()
    w = w.replace('  ', ' ')
    u = u.replace('  ', ' ')
    w = w.split(' ')
    u = u.split(' ')

    matches = len(set(w).intersection(set(u)))

    d = f'From {i}, we are adding to '
    for c in range(matches):
        d += str(i+c+1) + ' '
        copies[i+c+1] += copies[i]
    print(d)
    
    

print(ans)

"""
11700
29240
"""