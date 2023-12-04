from rich import print
f = open('input.dat', 'r')
lines = [x[:-1] for x in f.readlines()]
f.close()

ans = 0

for line in lines:
    _, info = line.split(':')
    info = info.split(';')
    info = [x.strip() for x in info]
    info = [x.replace(',','') for x in info]
    mins = {'blue':0, 'green':0, 'red':0}
    for game in info:
        g = game.split(' ')
        pairs = []
        for i in range(0, len(g), 2):
            pairs.append([int(g[i]), g[i+1]])
        for cnt, type in pairs:
            mins[type] = max(mins[type], cnt)
    ans += (mins['blue'] * mins['red'] * mins['green'])

print(ans)