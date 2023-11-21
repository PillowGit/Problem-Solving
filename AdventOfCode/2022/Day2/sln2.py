# 'A' = rock 
# 'B' = paper
# 'C' = scissors
# X = lose
# Y = draw
# Z = win

games = {
    'X': lambda c: 0 + (3 if c == 'A' else 1 if c == 'B' else 2),
    'Y': lambda c: 3 + (1 if c == 'A' else 2 if c == 'B' else 3),
    'Z': lambda c: 6 + (2 if c == 'A' else 3 if c == 'B' else 1)
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