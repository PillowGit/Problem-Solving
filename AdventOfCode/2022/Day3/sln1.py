f = open('input.dat', 'r')
lines = [l[:-1] for l in f.readlines()]
f.close()

ans = 0
for line in lines:
    m = len(line)//2
    chr = next(iter(set(line[:m]) & set(line[m:])))
    ans += (ord(chr) - ord('A') + 26 if chr.isupper() else ord(chr) - ord('a')) + 1
print(ans)