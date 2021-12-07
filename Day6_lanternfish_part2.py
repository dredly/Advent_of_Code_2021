from itertools import chain


def simulate_lanternfish(current, days_remaining):
    print(f'Days remaining: {days_remaining}')
    if days_remaining == 0:
        return len(list(current))
    else:
        current = chain(*([6, 8] if f == 0 else [f - 1] for f in current))
        return simulate_lanternfish(current, days_remaining - 1)


with open("lanternfish.txt") as fin:
    init_conditions = [int(x) for x in fin.read().split(",")]

init_conditions_test = [3, 4, 3, 1, 2]

print(simulate_lanternfish([0], 256))
