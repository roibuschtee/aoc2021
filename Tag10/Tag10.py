import numpy as np
from statistics import median
# data import

data = np.genfromtxt("Tag10/Tag10_daten.txt", dtype=str)

trans = "".maketrans("})]>", "{([<")
wrong_chars = []
tmp_section = []
corrupted_lines = []
for ind, line in enumerate(data):
    tmp_section = []
    for element in line:
        if element in ['{', '(', '[', '<']:
            tmp_section.append(element)
        else:
            if element.translate(trans) == tmp_section[-1]:
                tmp_section.pop()
            else:
                wrong_chars.append(element)
                corrupted_lines.append(ind)
                break

error_score = sum(list(map(lambda x: {')': 3, ']': 57, '}': 1197, '>':25137}[x], wrong_chars)))
print(error_score)

trans_inv = "".maketrans("{([<", "})]>")
score = []
for ind, line in enumerate(data):
    if ind not in corrupted_lines:
        tmp_section = []
        for element in line:
            if element in ['{', '(', '[', '<']:
                tmp_section.append(element)
            else:
                if element.translate(trans) == tmp_section[-1]:
                    tmp_section.pop()
        score.append(0)
        for element in reversed(tmp_section):
            score[-1] *= 5
            score[-1] += {'(': 1, '[': 2, '{': 3, '<':4}[element]

print(median(score))
