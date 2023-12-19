from rich import print
# input
lines = 0
with open('input.dat', 'r') as f:
    lines = [x[:-1] for x in f.readlines()]
# Build adj using ranges
adj = {}
for line in lines:
    if line == '': break
    key, dat = line.split('{')
    rules = dat.replace('}','').split(',')
    adj[key] = []
    for rule in rules:
        if ':' not in rule:
            adj[key].append(['','else',0,rule])
            break
        rule, dest = rule.split(':')
        c = rule[0]
        operator = rule[1]
        val = int(rule[2:])
        adj[key].append([c, operator, val, dest])
# Use a dfs to simulate ranges
def dfs(label, incoming):
    # We dont care about returns
    if label == 'R':
        return 0
    # Possibilities is the combination of all ranges if we reach
    # an accepted workflow
    if label == 'A':
        return len(incoming['x'])*len(incoming['m'])*len(incoming['a'])*len(incoming['s'])
    # Check other ranges
    total = 0
    # Convert our ranges into sets for easy overlap checking and pass by ref
    new_range = dict((k, set(v)) for (k,v) in incoming.items())
    # c is the letter in 'xmas' were looking at, operator is 
    # either <, >, or 'else' if its the last condition in the
    # workflow. val is self explanatory, dest is where it sends us
    for c, operator, val, dest in adj[label]:
        # if at last instruction just continue
        if operator == 'else':
            total += dfs(dest, new_range)
            break
        # otherwise make ranges for nums we would need
        elif operator == '>':
            rng = range(val+1, 4001)
        elif operator == '<':
            rng = range(1, val)
        # Construct new ranges to be passed into dfs
        sending = {}
        # This method will both construct a new range to be sent
        # and subtract the numbers we wont be using via `v.remove(i)` 
        # due to `in new_range.items()` passing a reference in python
        # since v is a set
        for k, v in new_range.items():
            if k != c:
                sending[k] = v
            else:
                sending[k] = set()
                for i in rng:
                    if i in v:
                        v.remove(i)
                        sending[k].add(i)
        total += dfs(dest, sending)
    return total
# Find answer
ans = dfs('in', {c:range(1,4001) for c in 'xmas'})
print(ans)