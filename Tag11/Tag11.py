import numpy as np
from statistics import median
# data import

data = np.genfromtxt("Tag11/Tag11_daten.txt", dtype=int, delimiter=1)

flashes = 0

for i in range(100):
    data += 1
    closed_list = []
    while True:
        element_visited = False
        for index, value in np.ndenumerate(data):
            if value > 9 and index not in closed_list:
                closed_list.append(index)
                tmp = data[max(0, index[0]-1):min(index[0]+1+1, data.shape[0]), max(0, index[1]-1):min(index[1]+1+1, data.shape[1])]
                tmp += 1
                element_visited = True
        if not element_visited:
            tmp = data[data>9]
            flashes += tmp.size
            if tmp.size == data.size:
                print(i)
            data[data>9] = 0
            break

print(flashes)


for i in range(1000):
    data += 1
    closed_list = []
    while True:
        element_visited = False
        for index, value in np.ndenumerate(data):
            if value > 9 and index not in closed_list:
                closed_list.append(index)
                tmp = data[max(0, index[0]-1):min(index[0]+1+1, data.shape[0]), max(0, index[1]-1):min(index[1]+1+1, data.shape[1])]
                tmp += 1
                element_visited = True
        if not element_visited:
            tmp = data[data>9]
            flashes += tmp.size
            if tmp.size == data.size:
                print(i+1+100)
                quit()
            data[data>9] = 0
            break