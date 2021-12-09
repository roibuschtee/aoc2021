import numpy as np
import itertools
import time
# data import
data = np.genfromtxt("Tag8/Tag8_daten.txt", delimiter=' ', dtype=None)

counter = 0
for line in data:  
    for element in itertools.islice(line, 11,15):
        if len(element) in [2,3,4,7]:
            counter += 1

print(counter)

counter = 0
for line in data:
    numbers = np.zeros(7, dtype=int)
    one = four = seven = set(b'')
    while np.sum(numbers) != 700:    
        for element in itertools.islice(line, 0,10):
            el_set = set(element)
            if len(element) == 2: #1
                one = el_set
                if numbers[5] != 0:
                    numbers[2] = list(one-set([numbers[5]]))[0]
            elif len(element) == 3: #7
                seven = el_set
                if len(one) > 0:
                    numbers[0] = list(seven-one)[0]
            elif len(element) == 6 and len(el_set.intersection(seven.union(four))) == 5: #9
                nine = el_set
                numbers[6] = list(nine-seven-four)[0]
            elif len(element) == 5 and len(el_set.intersection(one)) == 2: #3
                tmp = list(four-el_set)
                if len(tmp) == 1:
                    numbers[1] = tmp[0]
            elif len(element) == 4: #4
                four = el_set
                if numbers[1] != 0:
                    numbers[3] = list(el_set-one-set([numbers[1]]))[0]
            elif len(element) == 5 and len(el_set.intersection([numbers[1]])) == 1: #5
                tmp = list(el_set-set(numbers[[0,1,3,6]]))
                if len(tmp) == 1:
                    numbers[5] = tmp[0]
            if np.sum(numbers==0) == 1:
                numbers[4] = 700 - np.sum(numbers)

    translation = {x: chr(ind+97) for ind, x in enumerate(numbers)}
    number = 0
    for ind, element in enumerate(itertools.islice(line, 11,15)):
        
        tmp = element.decode()
        tmp_translated = ''.join(sorted(tmp.translate(translation)))
        if tmp_translated == 'cf':
            number += 1 * 10**(3-ind)
        elif tmp_translated == 'acf':
            number += 7 * 10**(3-ind)
        elif tmp_translated == 'abcefg':
            number += 0 * 10**(3-ind)
        elif tmp_translated == 'acdeg':
            number += 2 * 10**(3-ind)
        elif tmp_translated == 'acdfg':
            number += 3 * 10**(3-ind)
        elif tmp_translated == 'bcdf':
            number += 4 * 10**(3-ind)
        elif tmp_translated == 'abdfg':
            number += 5 * 10**(3-ind)
        elif tmp_translated == 'abdefg':
            number += 6 * 10**(3-ind)
        elif tmp_translated == 'abcdefg':
            number += 8 * 10**(3-ind)
        elif tmp_translated == 'abcdfg':
            number += 9 * 10**(3-ind)
    counter += number
print(counter)