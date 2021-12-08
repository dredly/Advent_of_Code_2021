from itertools import chain
from collections import Counter


def simulate_lanternfish(current, days_remaining):
    print(f"Days remaining: {days_remaining}")
    if days_remaining == 0:
        return current
    else:
        current = chain(*([6, 8] if f == 0 else [f - 1] for f in current))
        return simulate_lanternfish(current, days_remaining - 1)


def get_single_fish_dict(days, fish_nums):
    return {num: len(list(simulate_lanternfish([num], days))) for num in fish_nums}


with open("lanternfish.txt") as fin:
    init_conditions = [int(x) for x in fin.read().split(",")]

init_conditions_test = [3, 4, 3, 1, 2]
fish_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

fish_dict = get_single_fish_dict(128, fish_nums)
print("Simulating")
halfway = Counter(simulate_lanternfish(init_conditions, 128))
total = sum((v * fish_dict[k] for (k, v) in halfway.items()))
print("Done")
print(total)
