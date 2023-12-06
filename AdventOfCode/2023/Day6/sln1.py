from rich import print

f = open('input.dat', 'r')
lines = [x[:-1] for x in f.readlines()]
f.close()

times = lines[0].split(':')[1].strip()
tmp = []
cur = ''
for c in times+' ':
    if cur == '' and c == ' ': continue
    if c.isdigit():
        cur += c
    else:
        tmp.append(int(cur))
        cur = ''
times = tmp
tmp = []
cur = ''

dists = lines[1].split(':')[1].strip()
for c in dists+' ':
    if cur == '' and c == ' ': continue
    if c.isdigit():
        cur += c
    else:
        tmp.append(int(cur))
        cur = ''
dists = tmp

def solve(time, goal):
    wins = 0
    for i in range(time+1):
        if i*(time-i) > goal:
            wins += 1
    return wins

ans = 1
for time, goal in zip(times, dists):
    ans *= solve(time,goal)
print(ans)

"""
Wrong:
721280
Right:
449550
"""

# One Liner
print(eval('*'.join([str(c) for c in [(lambda t,d:sum(1 for i in range(t) if i*(t-i)>d))(i, j) for i, j in zip([int(x) for x in open('input.dat', 'r').readlines()[0].split(':')[1].strip().replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').split(' ')], [int(x) for x in open('input.dat', 'r').readlines()[1].split(':')[1].strip().replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').split(' ')])]])))