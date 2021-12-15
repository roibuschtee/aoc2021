import numpy as np
from statistics import median
from PIL import Image
# data import

def minCost(cost):
  
    rows = cost.shape[0]
    columns = cost.shape[1]
    tc = [[0 for x in range(columns)] for x in range(rows)]
  
    tc[-1][-1] = cost[-1][-1]
  
    for i in range(rows-2, -1, -1):
        tc[i][-1] = tc[i+1][-1] + cost[i][-1]
  
    for j in range(columns-2, -1, -1):
        tc[-1][j] = tc[-1][j+1] + cost[-1][j]
  
    for i in range(rows-2, -1, -1):
        for j in range(columns-2, -1, -1):
            tc[i][j] = min(tc[i+1][j], tc[i][j+1]) + cost[i][j]
  
    return tc[0][0]

data = np.genfromtxt("Tag15/Tag15_daten.txt", delimiter=1, dtype=int)

print(minCost(data)-data[0,0])

tmp_r = np.zeros((data.shape[0], 0), dtype=int)
tmp = data
for j in range(5):
    tmp[tmp >= 10] = 1
    tmp_r = np.hstack((tmp_r, tmp))
    tmp = tmp+1

tmp_m = np.zeros((0, tmp_r.shape[1]), dtype=int)
tmp = tmp_r
for j in range(5):
    tmp[tmp >= 10] = 1
    tmp_m = np.vstack((tmp_m, tmp))
    tmp = tmp+1

print(minCost(tmp_m)-data[-1,-1]+data[0,0])