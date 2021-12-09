import numpy as np
# data import
data = np.genfromtxt("Tag6/Tag5_daten.txt", delimiter=',', dtype=int)

fishes = np.zeros((9,1))

for i in range(9):
    for element in data:
        if element == i:
            fishes[i] += 1

# calculations
steps = 256
for i in range(steps):
    fishes = np.roll(fishes, -1)
    fishes[6] += fishes[-1]


print(np.sum(fishes))
