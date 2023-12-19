from rich import print

lines = 0
with open('input.dat', 'r') as f:
    lines = [x[:-1] for x in f.readlines()]
i = 0

# Build our workflow map
workflows = {}
for idx, line in enumerate(lines):
    if line == '':
        i = idx + 1
        break
    # Remove the key from the workflow process
    key, mapping = line.split('{')
    mapping = mapping[:-1]
    # Build lambda expressions
    process = 'lambda inp: '
    statements = mapping.split(',')
    for cmp in statements[:-1]:
        cond, ret = cmp.split(':')
        process += f'\'{ret}\' if inp[\'{cond[0]}\']{cond[1:]} else '
    process += '\''+statements[-1]+'\''
    # Add this lambda to our workflows
    workflows[key] = eval(process)

# Simulate each workflow
ans = 0
while i < len(lines):
    xmas = {pair.split(':')[0]:int(pair.split(':')[1]) for pair in lines[i].replace('=',':')[1:-1].split(',')}
    status = 'in'
    flow = 'in -> '
    while status != 'A' and status != 'R':
        status = workflows[status](xmas)
        flow += status + ' -> '
    if status =='A':
        ans += sum(xmas.values())
    print(xmas)
    print(flow[:-3])
    i += 1
print(ans)