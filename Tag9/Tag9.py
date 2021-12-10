import numpy as np
import itertools
import time
import scipy.ndimage.filters as filters
import scipy.ndimage.morphology as morphology
# data import

data = np.empty((0,0), dtype=int)
with open("Tag9/Tag9_daten.txt", 'r') as f:
    for line in (line.rstrip('\n') for line in f):
        if data.size == 0:
            data.resize(0, len(line))
        line_int = [int(char) for char in line]
        data = np.vstack([data, line_int])

neighborhood = morphology.generate_binary_structure(len(data.shape),2)
neighborhood[0][[0,2]] = False
neighborhood[2][[0,2]] = False
def fun(buffer):
    m_buffer = np.amin(buffer)
    len_min = len(*np.where(buffer == m_buffer))
    return 1e8 if len_min > 1 else m_buffer
local_min = (filters.generic_filter(data, fun, footprint=neighborhood, mode='constant', cval=1e8)==data)

sum_risk = 0
for index, value in np.ndenumerate(data):
    if local_min[index]:
        sum_risk += 1+value
print(sum_risk)

sizes = []
for index, value in np.ndenumerate(data):
    if local_min[index]:
        tmp = data[max(0, index[0]-10):min(index[0]+10, data.shape[0]), max(0, index[1]-10):min(index[1]+10, data.shape[1])]
        a = index[0] - max(0, index[0]-10)
        b = index[1] - max(0, index[1]-10)
        open_list = [(a,b)]
        closed_list = []
        size = 1
        while len(open_list) > 0:
            current_idx = open_list.pop()
            closed_list.append(current_idx)
            for i in range(0,11):
                if current_idx[0]+i>=tmp.shape[0]:
                    break
                if tmp[(current_idx[0]+i, current_idx[1])] >= 9:
                    break
                for j in range(0,11):
                    tmp_idx = (current_idx[0]+i, current_idx[1]+j)
                    if (i!=0 or j!=0) and tmp_idx not in closed_list and tmp_idx not in open_list and tmp_idx[0] >= 0 and tmp_idx[1] >= 0 and tmp_idx[0] < tmp.shape[0] and tmp_idx[1] < tmp.shape[1]:
                        if tmp[tmp_idx] < 9:
                            size += 1
                            open_list.append(tmp_idx)
                        else:
                            break
                    elif tmp_idx[0] >= 0 and tmp_idx[1] >= 0 and tmp_idx[0] < tmp.shape[0] and tmp_idx[1] < tmp.shape[1] and tmp[tmp_idx] >= 9:
                        break
            for i in range(0,-11,-1):
                if current_idx[0]+i<0:
                    break
                if tmp[(current_idx[0]+i, current_idx[1])] >= 9:
                    break
                for j in range(0,-11,-1):
                    tmp_idx = (current_idx[0]+i, current_idx[1]+j)
                    if (i!=0 or j!=0) and tmp_idx not in closed_list and tmp_idx not in open_list and tmp_idx[0] >= 0 and tmp_idx[1] >= 0 and tmp_idx[0] < tmp.shape[0] and tmp_idx[1] < tmp.shape[1] and tmp[tmp_idx] < 9:
                        if tmp[tmp_idx] < 9:
                            size += 1
                            open_list.append(tmp_idx)
                        else:
                            break
                    elif tmp_idx[0] >= 0 and tmp_idx[1] >= 0 and tmp_idx[0] < tmp.shape[0] and tmp_idx[1] < tmp.shape[1] and tmp[tmp_idx] >= 9:
                        break
        sizes.append(size)
sizes.sort()
print(np.prod(sizes[-3:]))