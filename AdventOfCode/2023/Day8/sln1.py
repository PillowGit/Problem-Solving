from rich import print

f = open('input.dat', 'r')
lines = [x[:-1] for x in f.readlines()]
f.close()

instructions = lines[0]
directions = {}
way = lambda z:1 if z == 'R' else 0
for line in lines[2:]:
    f, t = line.split('=')
    f=f.strip()
    t=t.strip()
    t=t.replace('(','')
    t=t.replace(')','')
    t=t.replace(',','')
    t=t.split(' ')
    directions[f] = t

i = 0
cur = 'AAA'
while cur != 'ZZZ':
    cur = directions[cur][way(instructions[i%len(instructions)])]
    i += 1
print(i)