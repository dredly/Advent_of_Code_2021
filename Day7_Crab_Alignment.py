from statistics import median


def get_fuel_cost(alignments):
    median_alignment = int(median(alignments))
    return sum((abs(a - median_alignment) for a in alignments))


def get_fuel_cost_2(alignments, search_range):
    median_alignment = int(median(alignments))
    current_min = 1000000000000
    for i in range(
        int(median_alignment - 0.5 * search_range),
        int(median_alignment + 0.5 * search_range),
    ):
        fuel_cost = sum((sum(range(abs(a - i) + 1)) for a in alignments))
        if fuel_cost < current_min:
            current_min = fuel_cost
    return current_min


with open("crab_data.txt") as fin:
    data = [int(x) for x in fin.read().split(",")]

data_test = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

# print(get_fuel_cost(data))
print(get_fuel_cost_2(data, 300))
