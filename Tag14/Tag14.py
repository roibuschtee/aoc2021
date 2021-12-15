import numpy as np
from copy import deepcopy
import math
import functools

filename = "Tag14/Tag14_daten.txt"
data = np.genfromtxt(filename, dtype=str, delimiter=" -> ", skip_header=2)

start_poly = ""
with open(filename) as f:
    start_poly = f.readline().strip()

assignment = dict()
for element in data:
    assignment[element[0]] = [[element[0][0]+element[1], element[1]+element[0][1]],0]

tmp = start_poly
for i in range(len(start_poly)-1):
    assignment[tmp[i:i+2]][1] += 1

for i in range(40):
    tmp_assignment = deepcopy(assignment)
    for element in tmp_assignment.items():
        count = element[1][1]
        assignment[element[1][0][0]][1] += count
        assignment[element[1][0][1]][1] += count
        assignment[element[0]][1] -= count

chars = set(functools.reduce(lambda a,b: a+b, assignment))
tmp = [0]*len(chars)
for key in assignment:
    for ind, char in enumerate(chars):
        if char in key:
            tmp[ind] += assignment[key][1]*key.count(char)
tmp = [math.ceil(x/2) for x in tmp]
print(max(tmp)-min(tmp))


'''
tmp = start_poly
tmp1 = [[]]*data.shape[0]
for i in range(10):
    for ind, element in enumerate(data):
        tmp1[ind] = [i for i in range(len(tmp)-1) if tmp[i:i+2] == element[0]]
    for ind, element in enumerate(tmp1):
        for ind1, element1 in enumerate(element):
            tmp = tmp[0:element1+1] + data[ind][1] + tmp[element1+1:]
            for ind2, element2 in enumerate(tmp1):
                for ind3, element3 in enumerate(element2):
                    if element3 > element1:
                        tmp1[ind2][ind3] += 1

chars = set(tmp)
nums = [tmp.count(x) for x in chars]
print(max(nums)-min(nums))
'''