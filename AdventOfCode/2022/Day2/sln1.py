# 'A' = rock = 'X'
# 'B' = paper = 'Y'
# 'C' = scissors = 'Z'

games = {
    'X': lambda c: 1 + (6 if c == 'C' else 3 if c == 'A' else 0),
    'Y': lambda c: 2 + (6 if c == 'A' else 3 if c == 'B' else 0),
    'Z': lambda c: 3 + (6 if c == 'B' else 3 if c == 'C' else 0)
}

sm = 0
f = open('input.dat', 'r')
lines = f.readlines()
f.close()

for line in lines:
    o, u = line[:-1].split(' ')
    #print(f'You played {u}, your opponent played {o}. You are expected to gain {games[u](o)} points for this match')
    sm += games[u](o)

print(f'Your expected score is {sm}')