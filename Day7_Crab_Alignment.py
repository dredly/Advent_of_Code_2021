from statistics import median


def get_fuel_cost(alignments):
    median_alignment = int(median(alignments))
    return sum((abs(a - median_alignment) for a in alignments))


with open("crab_data.txt") as fin:
    data = [int(x) for x in fin.read().split(",")]

data_test = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

print(get_fuel_cost(data))
