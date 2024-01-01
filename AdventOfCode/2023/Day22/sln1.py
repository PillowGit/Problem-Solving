from rich import print

lines = 0
with open('input.dat', 'r') as f:
    lines = [x[:-1] for x in f.readlines()]
# Define a brick (crazy)
class Brick:
    def __init__(self, l, r):
        self.xrange = list(range(l[0], r[0]+1))
        self.yrange = list(range(l[1], r[1]+1))
        self.h0 = l[2]
        self.h1 = r[2]
        self.supp = [] # Bricks that we support
        self.rest = [] # Blocks we are resting on
    # Functions to easily determine height of brick
    def minh(self):
        return min(self.h0, self.h1)
    def maxh(self):
        return max(self.h0, self.h1)
    #  Function to tell if a brick is overlapping with another
    def overlaps(self, other: 'Brick'):
        in_x, in_y = False, False
        for x in self.xrange:
            if x in other.xrange:
                in_x = True
                break
        if not in_x:
            return False
        else:
            for y in self.yrange:
                if y in other.yrange:
                    in_y = True
                    break
            return in_y
# Make all the bricks using the input
bricks: list['Brick'] = []
for line in lines:
    l,r = line.split('~')
    l = [int(x) for x in l.split(',')]
    r = [int(x) for x in r.split(',')]
    bricks.append(Brick(l,r))
bricks.sort(key=lambda b:b.minh())
# Function to drop all the bricks
def drop_bricks():
    for n, cur_brick in enumerate(bricks):
        # look at bricks that come after this one to figure out if it'll fall on top of it
        for i in range(n-1, -1, -1):
            # Our curr height
            rest_at = cur_brick.rest[0].maxh() if len(cur_brick.rest) != 0 else 1
            # If we will hit this brick while dropping
            if cur_brick.overlaps(bricks[i]):
                # Determine the height we'd land at
                new_rest_at = bricks[i].maxh()
                # If we are resting on nothing rn or this is a new max height we would rest on
                if len(cur_brick.rest) == 0 or new_rest_at > rest_at:
                    # Remove ourselves from the list of supported bricks from every brick we were previously resting on
                    for old_resting_on in cur_brick.rest:
                        old_resting_on.supp.remove(cur_brick)
                    # Note that we are resting on this brick
                    cur_brick.rest = []
                    cur_brick.rest.append(bricks[i])
                    # Tell this brick its supporting us
                    bricks[i].supp.append(cur_brick)
                # If we find another brick that can support us at once
                elif new_rest_at == rest_at:
                    # Tell it that it's also supporting us now
                    bricks[i].supp.append(cur_brick)
                    # And note that we're resting on it
                    cur_brick.rest.append(bricks[i])
        # Determine where our height is now
        diff = cur_brick.minh() - (cur_brick.rest[0].maxh() + 1) if cur_brick.rest else cur_brick.minh() - 1
        cur_brick.h0 -= diff
        cur_brick.h1 -= diff
# Drop all blocks then determine our answer
ans = 0
drop_bricks()
for b in bricks:
    # if all the bricks we support have more than 1 resting brick then we dont care if this one disappears, add it to total
    if all([len(x.rest) > 1 for x in b.supp]):
        ans += 1
print(ans)
"""
Wrong:
506
580
"""