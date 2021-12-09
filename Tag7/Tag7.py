import numpy as np
# data import
data = np.genfromtxt("Tag7/Tag7_daten.txt", delimiter=',', dtype=int)

min_data = np.min(data)
boxes = np.zeros((np.max(data)-min_data+1,1))

for element in data:
    boxes[element-min_data] += 1

cost = np.zeros(boxes.size)

for position in range(len(cost)):
    for ind, element in enumerate(boxes):
        cost[position] += np.abs(position-ind)*element

cost_min = np.min(cost)

print(cost_min)

cost = np.zeros(boxes.size)

for position in range(len(cost)):
    for ind, element in enumerate(boxes):
        cost[position] += np.sum(np.arange(np.abs(position-ind)+1))*element

cost_min = np.min(cost)

print(cost_min)