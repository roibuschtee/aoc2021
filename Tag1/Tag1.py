import numpy as np

#data and functions
def get_window(seq, n):
    for i in range(len(seq)-n+1):
        yield np.sum(seq[i:i+n])

data = np.genfromtxt("Tag1_daten.txt", delimiter='\n')
# task 1
greater = np.sum(np.diff(data)>0)
print(greater)

#task 2
greater_second = 0
window_generator = get_window(data, 3)
last_sum = next(window_generator)
for current_sum in window_generator:
    if current_sum > last_sum:
        greater_second += 1
    last_sum = current_sum

#task 2 alternative
greater_second = 0
last_sum = np.sum(data[0:3])
for i in range(len(data)-2):
    current_sum = np.sum(data[i:i+3])
    if current_sum > last_sum:
        greater_second += 1
    last_sum = current_sum

print(greater_second)