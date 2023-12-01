from rich import print

f = open('input.dat', 'r')
lines = [x[:-1] for x in f.readlines()]
f.close()

ans = 0

def convert_and_filter(inp:str):
    nums  = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    res = []
    cur = ''
    for c in inp:
        if not c.isalpha():
            res.append(int(c))
            cur = ''
        else:
            cur += c
            for k, v in nums.items():
                if k in cur:
                    res.append(v)
                    cur = c
                    break
    print(f'{inp} -> {res}')
    return res

for line in lines:
    parsed = convert_and_filter(line)
    ans += parsed[0]*10 + parsed[-1]

print(ans)

"""
Wrong answers:
51149
"""