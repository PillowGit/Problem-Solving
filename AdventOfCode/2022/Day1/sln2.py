from heapq import heappush, heappop

f = open('input.dat', 'r')
lines = f.readlines()
f.close()

elves = []
curr = 0
for line in lines:
    if line == '\n':
        heappush(elves, -curr)
        curr = 0
    else:
        curr += int(line[:-1])

e1, e2, e3 = -heappop(elves), -heappop(elves), -heappop(elves)
print(f'The elves with the most calories have {e1}, {e2}, and {e3}. The sum of these is {e1+e2+e3}')