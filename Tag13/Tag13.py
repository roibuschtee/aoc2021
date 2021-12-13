import numpy as np
from statistics import median
from PIL import Image
# data import

test = False
first = False

data = []
fold = []
with open("Tag13/Tag13_daten_test.txt" if test else "Tag13/Tag13_daten.txt", 'r') as f:
    part = 0
    for line in (line.rstrip('\n') for line in f):
        if len(line) == 0:
            part += 1
            continue
        if part == 0:
            cord = tuple(map(int, line.split(",")))
            data.append(cord)
        else:
            fold.append(line.split(" ")[2].split("="))

max_size = np.max(data, axis=0)+1
if not test:
    max_size[0] = max(max_size[0], int(fold[0][1])*2+1)
    max_size[1] = max(max_size[1], int(fold[1][1])*2+1)

paper = np.zeros(max_size, dtype=bool)

for element in data:
    paper[element] = True

if first:
    fold = [fold[0]]

for element in fold:
    if element[0] == 'x':
        paper = paper[0:int(element[1]), :] | paper[-1:int(element[1]):-1, :]
    else:
        paper = paper[:, 0:int(element[1])] | paper[:, -1:int(element[1]):-1]


p = np.transpose(paper)
print(np.count_nonzero(paper))

if not first:

    def img_grey(data):
        return Image.fromarray(np.uint8(data) * 255, mode='L').convert('1')

    img = img_grey(p)
    img.show()