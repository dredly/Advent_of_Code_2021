import numpy
from statistics import mode

def bin_diagnostic(data):
    data_arr = numpy.transpose(numpy.array([list(entry) for entry in data]))
    gamma = ''.join((mode(row) for row in data_arr))
    epsilon = ''.join(('1' if i == '0' else '0' for i in gamma))
    return int(gamma, 2) * int(epsilon, 2)

current = 0
def get_ratings(data, is_most):
    global current
    if len(data) == 1:
        current = 0
        return int(data[0], 2)
    if is_most:
        current_column = [row[current] for row in data]
        if current_column.count('1') >= current_column.count('0'):
            new_data = [row for row in data if row[current] == '1']
            current += 1
            return get_ratings(new_data, is_most)
        new_data = [row for row in data if row[current] == '0']
        current += 1
        return get_ratings(new_data, is_most)
    else:
        current_column = [row[current] for row in data]
        if current_column.count('0') <= current_column.count('1'):
            new_data = [row for row in data if row[current] == '0']
            current += 1
            return get_ratings(new_data, is_most)
        new_data = [row for row in data if row[current] == '1']
        current += 1
        return get_ratings(new_data, is_most)


def life_support_rating(data):
    return get_ratings(data, True) * get_ratings(data, False)

    
with open('bin_data.txt') as fin:
    real_data = [line.strip() for line in fin.readlines()]

test_data = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010'
]

#print(bin_diagnostic(real_data))
print(life_support_rating(real_data))
