import numpy as np

data = np.genfromtxt("Tag2/Tag2_daten.txt", dtype=[('mystring', 'U10'),('myfloat','i8')])

pos = [0, 0]

for element in data:
    if "forward" in element[0]:
        pos[0] += element[1]
    elif "down" in element[0]:
        pos[1] += element[1]
    elif "up" in element[0]:
        pos[1] -= element[1]

print(np.product(pos))

pos_aim = [0, 0, 0]
for element in data:
    if "forward" in element[0]:
        pos_aim[0] += element[1]
        pos_aim[1] += element[1] * pos_aim[2]
    elif "down" in element[0]:
        pos_aim[2] += element[1]
    elif "up" in element[0]:
        pos_aim[2] -= element[1]

print(pos_aim[0]*pos_aim[1])