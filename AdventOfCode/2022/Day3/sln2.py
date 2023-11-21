f = open('input.dat', 'r')
lines = [l[:-1] for l in f.readlines()]
f.close()

ans = 0
for i in range(0, len(lines), 3):
    chr = next(iter(set(lines[i]) & set(lines[i+1]) & set(lines[i+2])))
    ans += (ord(chr) - ord('A') + 26 if chr.isupper() else ord(chr) - ord('a')) + 1
print(ans)