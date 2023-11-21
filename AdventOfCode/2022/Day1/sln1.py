f = open('input.dat', 'r')
lines = f.readlines()
f.close()

elves = []
curr = 0
for line in lines:
    if line == '\n':
        elves.append(curr)
        curr = 0
    else:
        curr += int(line[:-1])

print(f'The elf with this most calories has {max(elves)}')