from rich import print

f = open('input.dat', 'r')
lines = [x[:-1] for x in f.readlines()]
f.close()

def make_history(nums: list[int]) -> list[list[int]]:
    hist = [nums]
    while True:
        layer = []
        final = True
        for i in range(1, len(hist[-1])):
            diff = hist[-1][i] - hist[-1][i-1]
            if diff != 0:
                final = False
            layer.append(diff)
        hist.append(layer)
        if final: break
        layer = []
    return hist

def final(history: list[list[int]]) -> int:
    ans = 0
    for row in history[::-1]:
        if not row: continue
        ans = row[0] - ans
    return ans

total = 0
for line in lines:
    arr = [int(x) for x in line.split()]
    hist = make_history(arr)
    total += final(hist)
print(total)

"""
wrong
1959794152
2871827298400
3548952092399
"""