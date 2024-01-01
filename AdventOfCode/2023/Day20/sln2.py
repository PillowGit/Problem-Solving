from collections import deque
from rich import print
from math import lcm

lines = 0
with open('input.dat', 'r') as f:
    lines = [x[:-1].split(' -> ') for x in f.readlines()]
# Define how a module works
class Module:
    pulses = {'low':0, 'high':0}
    def __init__(self, label: str, type: str, connections: list[str]):
        self.label = label
        self.type = type # can be '%' or '&'
        if self.type == '&':
            self.memory = {}
        elif self.type == '%':
            self.state = 'off'
        else:
            raise Exception('unknown module type')
        self.connections = connections
    def __str__(self):
        if self.type == '%':
            return f'Module(label={self.label}, type={self.type}, connections=[{",".join(self.connections)}], state={self.state})'
        else:
            return f'Module(label={self.label}, type={self.type}, connections=[{",".join(self.connections)}], mem={self.memory})'
    def __repr__(self): return self.__str__()
    def add_mem(self, label: str):
        if self.type == '&' and label not in self.memory: self.memory[label] = 'low'
    def recieve_pulse(self, sender: str, pulse: str) -> str:
        if self.type == '&':
            self.memory[sender] = pulse
            if 'low' in self.memory.values():
                return 'high'
            else:
                return 'low'
        elif self.type == '%':
            if pulse == 'high':
                return None
            elif pulse == 'low':
                if self.state == 'off':
                    self.state = 'on'
                    return 'high'
                else:
                    self.state = 'off'
                    return 'low'
# Create all modules first
modules = {}
broadcaster = []
for mod, outs in lines:
    outs = outs.replace(' ','')
    if mod == 'broadcaster': 
        broadcaster = outs.split(',')
        continue
    type = mod[0]
    label = mod[1:]
    connections = outs.split(',')
    modules[label] = Module(label,type,connections)
# Build memory for & modules
for f, t in lines:
    if f == 'broadcaster': continue
    for outgoing in t.replace(' ','').split(','): 
        if outgoing in modules: modules[outgoing].add_mem(f[1:])
for m in broadcaster:
    if m in modules:
        modules[m].add_mem('broadcaster')
# For part 2, xr needs to a low pulse.
# For xr to get a low pulse, mg is responsible for this.
# mg will send a low pulse if its memory is all high pulses
# there are 4 modules that will send pulses to mg, so we will stop once xr_conds has 4 modules in it
# when a module sends a high pulse to mg, record which button press this happens
# once mg remembers when each module has sent its low pulses to it, we can use lcm to figure out
# when they will happen simultaneously
xr_conds = {}
# Define how to simulate a button press
def simulate(i):
    # Queue is of format [from, to, pulse]
    on = False
    q = deque()
    Module.pulses['low'] += 1
    for m in broadcaster:
        q.append(['broadcaster', m,'low'])
    while q:
        sender, reciever, pulse = q.popleft()
        # wishful thinking :(
        if reciever == 'rx' and pulse == 'low':
            on = True
            break
        Module.pulses[pulse] += 1
        if reciever not in modules: continue
        res = modules[reciever].recieve_pulse(sender, pulse)
        # If prereq module for xr sends the pulse we need (high) then add when it happened
        if reciever == 'mg' and pulse == 'high':
            xr_conds[sender] = i
        if res:
            for conn in modules[reciever].connections:
                q.append([reciever, conn, res])
    return on
# Get answer
for i in range(1,999999999):
    if len(xr_conds) == 4: break
    else: simulate(i)
print(lcm(*list(xr_conds.values())))
