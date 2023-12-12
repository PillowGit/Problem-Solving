from functools import cache
from rich import print

lines = 0
with open('input.dat', 'r') as f:
    lines = [x[:-1] for x in f.readlines()]

@cache
def solve(record, groups, i, length, group):
    if i == len(record): # At end of spring record
        ans = 1 if len(groups) == group else 0 # ret 1 if we could place all groups of broken springs but 0 if not
    elif record[i] == '#': #omg we can put something here :3
        ans = solve(record, groups, i + 1, length + 1, group) # put spring here
    elif record[i] == '.' or group == len(groups): # if done evaluating last group
        if group < len(groups) and length == groups[group]: # not the last group of broken springs but we did place this entire group
            ans = solve(record, groups, i + 1, 0, group + 1) # start looking for the next group
        elif length == 0: # wait we havent found any spots to put broken springs in
            ans = solve(record, groups, i + 1, 0, group) # just slide index over 1
        else:
            ans = 0 # we couldnt fit in the group at ALL
    else:
        hash_count = solve(record, groups, i + 1, length + 1, group) # keep looking for current group
        dot_count = 0 # count possibilities if we just look for next group now
        if length == groups[group]: # if we even can look for the next group
            dot_count = solve(record, groups, i + 1, 0, group + 1)
        elif length == 0:  # or if we haven't even started looking at our current group of broken springs
            dot_count = solve(record, groups, i + 1, 0, group) # just slide our start index over 1 and look for those possibilities
        ans = hash_count + dot_count # Add the possibilities
    return ans
            
ans = 0
for line in lines:
    mapping, groups = line.split(' ')
    mapping = [mapping]*5
    groups = [int(x) for x in groups.split(',')]*5
    ans += solve('?'.join(mapping) + '.', tuple(groups), 0, 0, 0)
print(ans)

#THIS TOOKFUCKING FOREVER