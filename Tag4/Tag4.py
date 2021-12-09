import numpy as np

data = np.genfromtxt("Tag4/Tag4_daten_test.txt", skip_header=2)

data1 = data.reshape((data.size//25,5,5))

a=1