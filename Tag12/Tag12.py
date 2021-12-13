import numpy as np
from statistics import median
# data import

def step(graph, node, visited, goal, single_visit):
    neighbours = []
    paths = []
    visited.add(node)
    for element in graph[node]:
        if element in single_visit and element in visited:
            continue
        elif element == goal:
            paths.append([node, element])
        else:
            tmp_paths = step(graph, element, visited.copy(), goal, single_visit)
            paths += [[node]+x for x in tmp_paths]
            a=1
            
    return paths


data = np.genfromtxt("Tag12/Tag12_daten.txt", dtype=str, delimiter="-")
data_ = np.zeros(data.shape, dtype=int)
nodes = np.unique(data)
tmp = {val:i for i,val in enumerate(nodes)}

graph = {i: [] for i in range(len(nodes))}

for ind, element in np.ndenumerate(data):
    data_[ind] = tmp[element]

for element in data_:
    graph[element[0]].append(element[1])
    graph[element[1]].append(element[0])

single_visit = [i for i in range(len(nodes)) if 96 < ord(nodes[i][0]) < 123 ]

start = np.where(nodes == 'start')[0][0]
ende = np.where(nodes == 'end')[0][0]

paths = step(graph, start, set([]), ende, single_visit)

print(len(paths))

#TODO: Teil2

