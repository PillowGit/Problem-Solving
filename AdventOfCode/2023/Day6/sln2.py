from rich import print

f = open('input.dat', 'r')
lines = [x[:-1] for x in f.readlines()]
f.close()

time = int(lines[0].split(':')[1].replace(' ', ''))
dist = int(lines[1].split(':')[1].replace(' ', ''))

lower = 0
for i in range(time+1):
    if i*(time-i) > dist:
        lower = i
        break

upper = 0
for i in range(time+1, -1, -1):
    if i*(time-i) > dist:
        upper = i
        break

print(upper - lower + 1)

# One Liner
print((lambda t,d:sum(1 for i in range(t) if i*(t-i)>d))(int(open('input.dat','r').readlines()[0].split(':')[1].replace(' ','')),int(open('input.dat','r').readlines()[1].split(':')[1].replace(' ',''))))