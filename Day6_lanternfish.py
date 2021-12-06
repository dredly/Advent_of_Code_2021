import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def exponential(x, a, b):
    return a * np.exp(b * x)


def simulate_lanternfish(init_conditions, num_days):
    current_fish = init_conditions
    lengths = [len(init_conditions)]
    for day in range(1, num_days + 1):
        zero_count = current_fish.count(0)
        current_fish = [f - 1 if f != 0 else 6 for f in current_fish] + [8] * zero_count
        lengths.append(len(current_fish))
    return lengths


with open("lanternfish.txt") as fin:
    init_conditions = [int(x) for x in fin.read().split(",")]

init_conditions_test = [3, 4, 3, 1, 2]

x = np.linspace(0, 150, 150)
print(len(x))
plt.plot(x, simulate_lanternfish([0], 149))
plt.show()
