import numpy as np
from functools import reduce
from operator import add, sub
data = np.genfromtxt("Tag3/Tag3_daten.txt", dtype='str')

ones = reduce(lambda x,y: list(map(add,x,y)), list(map(lambda x: [int(bit=='1') for bit in x], data)))
zeros = list(map(lambda x: len(data) - x, ones))
output = ''.join(['0' if z > o else '1' for o,z in zip(ones,zeros)])
output_eps = ''.join(['1' if z > o else '0' for o,z in zip(ones,zeros)])
gamma = int(output, 2)
eps = int(output_eps, 2)

print(gamma*eps)

data1 = data

for i in range(len(data[0])):
    j = 0
    z = 0
    o = 0
    c = '1'
    for element in data1:
        if element[i] == '1':
            o += 1
        else:
            z += 1
    if z > o:
        c = '0'
    while j < len(data1):
        if data1[j][i] != c:
            data1 = np.delete(data1, j)
            continue
        j += 1
data2 = data
for i in range(len(data[0])):
    j = 0
    z = 0
    o = 0
    c = '0'
    for element in data2:
        if element[i] == '1':
            o += 1
        else:
            z += 1
    if o < z:
        c = '1'
    while j < len(data2):
        if len(data2) == 1:
            break
        if data2[j][i] != c:
            data2 = np.delete(data2, j)
            continue
        j += 1

ox = int(data1[0], 2)
co2 = int(data2[0], 2)

print(ox*co2)