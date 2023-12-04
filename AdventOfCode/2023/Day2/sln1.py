from rich import print
f = open('input.dat', 'r')
lines = [x[:-1] for x in f.readlines()]
f.close()

ans = 0
t = {'red':12, 'green':13, 'blue':14}

for line in lines:
    gameid, info = line.split(':')
    gameid = int(gameid.split(' ')[1])
    info = info.split(';')
    info = [x.strip() for x in info]
    info = [x.replace(',','') for x in info]
    print(f'Testing game {gameid}')
    valid = True
    for game in info:
        print(f'Analyzing {game}')
        g = game.split(' ')
        pairs = []
        for i in range(0, len(g), 2):
            pairs.append([int(g[i]), g[i+1]])
        print(f'Came up with {pairs}')
        for cnt, type in pairs:
            if cnt > t[type]:
                valid = False
    if valid: ans += gameid

print(ans)