from rich import print

lines = 0
with open('input.dat', 'r') as f:
    lines = [x[:-1] for x in f.readlines()]
lines = [[c for c in line] for line in lines]
n = len(lines)

def tilt():
    for j in range(len(lines[0])):
        pos = 0
        for i in range(len(lines)):
            if lines[i][j] == '#':
                pos = i + 1
            elif lines[i][j] == 'O':
                lines[i][j] = '.'
                lines[pos][j] = 'O'
                pos += 1

def load() -> int:
    res = 0
    for i in range(len(lines)):
        res += lines[i].count('O') * (n - i)
    return res

def rotate():
    global lines
    grid = [['.' for _ in range(len(lines))] for _ in range(len(lines[0]))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[j][n-i-1] = lines[i][j]
    lines = grid

def str_grid():
    return '\n'.join(''.join(x for x in line) for line in lines)

cycle = 1
seen = {}
while True:
    for _ in range(4):
        tilt()
        rotate()
    curr_rocks = str_grid()
    print(curr_rocks)
    if curr_rocks in seen:
        curr_cycle = cycle - seen[curr_rocks][0]
        for cycle_, ans in seen.values():
            if cycle_ >= seen[curr_rocks][0] and cycle_ % curr_cycle == 1000000000 % curr_cycle:
                print(ans)
        break
    else:
        seen[curr_rocks] = (cycle, load())
        cycle += 1

"""
wrong:
111161
"""