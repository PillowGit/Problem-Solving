f = open('input.dat', 'r')
lines = [x[:-1] for x in f.readlines()]
f.close()

ans = 0
for line in lines:
    i = ''.join(char for char in line if not char.isalpha())
    ans += i[0] if len(i) < 2 else i[0]*10+i[-1]
print(ans)