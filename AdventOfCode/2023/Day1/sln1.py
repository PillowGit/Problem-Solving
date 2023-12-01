f = open('input.dat', 'r')
lines = [x[:-1] for x in f.readlines()]
f.close()


ans = 0
for line in lines:
    i = ''.join(char for char in line if not char.isalpha())
    ans += int(i[0]+i[-1])
print(ans)

# One line version
print(sum((lambda x:int(x[0]+x[-1]))([c for c in line if not c.isalpha() and c != '\n']) for line in [l[:-1] for l in open('input.dat', 'r').readlines()]))