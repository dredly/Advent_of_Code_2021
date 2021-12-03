import numpy
from statistics import mode

def bin_diagnostic(data):
    data_arr = numpy.transpose(numpy.array([list(entry) for entry in data]))
    gamma = ''.join((mode(row) for row in data_arr))
    epsilon = ''.join(('1' if i == '0' else '0' for i in gamma))
    return int(gamma, 2) * int(epsilon, 2)
    
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

print(bin_diagnostic(real_data))