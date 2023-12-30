import networkx as nx
from rich import print
# input
lines = 0
with open('input.dat', 'r') as f:
    lines = [x[:-1] for x in f.readlines()]
# parse
graph = nx.Graph()
for line in lines:
    src, dest = line.split(':')
    dest = dest.strip().split(' ')
    for d in dest: graph.add_edge(src, d)
# get answer cuz library is op
cuts = nx.minimum_edge_cut(graph)
graph.remove_edges_from(cuts)
components = list(nx.connected_components(graph))
print(len(components[0])*len(components[1]))