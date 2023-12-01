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
    #print(f'{inp} -> {res}')
    return res

for line in lines:
    parsed = convert_and_filter(line)
    ans += parsed[0]*10 + parsed[-1]

print(ans)


# One line version
print(sum([(lambda x:int(line[x]) if line[x].isnumeric() else 0 if line[x] == 'z' else 1 if line[x] == 'o' else 2 if line[x:x+2] == 'tw' else 3 if line[x:x+2] == 'th' else 4 if line[x:x+2] == 'fo' else 5 if line[x:x+2] == 'fi' else 6 if line[x:x+2] == 'si' else 8 if line[x] == 'e' else 9 if line[x] == 'n' else 7)(min(list(filter(lambda x:x!=-1,[line.find('0'),line.find('1'),line.find('2'),line.find('3'),line.find('4'),line.find('5'),line.find('6'),line.find('7'),line.find('8'),line.find('9'),line.find('0'),line.find('one'),line.find('two'),line.find('three'),line.find('four'),line.find('five'),line.find('six'),line.find('seven'),line.find('eight'),line.find('nine'),line.find('zero')]))))*10+(lambda x:int(line[x]) if line[x].isnumeric() else 0 if line[x] == 'z' else 1 if line[x] == 'o' else 2 if line[x:x+2] == 'tw' else 3 if line[x:x+2] == 'th' else 4 if line[x:x+2] == 'fo' else 5 if line[x:x+2] == 'fi' else 6 if line[x:x+2] == 'si' else 8 if line[x] == 'e' else 9 if line[x] == 'n' else 7)(max(line.rfind('0'),line.rfind('1'),line.rfind('2'),line.rfind('3'),line.rfind('4'),line.rfind('5'),line.rfind('6'),line.rfind('7'),line.rfind('8'),line.rfind('9'),line.rfind('0'),line.rfind('one'),line.rfind('two'),line.rfind('three'),line.rfind('four'),line.rfind('five'),line.rfind('six'),line.rfind('seven'),line.rfind('eight'),line.rfind('nine'),line.rfind('zero'))) for line in [z[:-1] for z in open('input.dat','r').readlines()]]))
