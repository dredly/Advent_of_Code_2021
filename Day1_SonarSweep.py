def sonar_sweep(depths):
    return len([d for idx, d in enumerate(depths) if idx > 0 and d > depths[idx - 1]])


def group_by_n(depths, n):
    sums = [
        sum(depths[idx + 1 - n : idx + 1]) for idx in range(len(depths)) if idx >= 2
    ]
    return sums


with open("depths_input.txt") as fin:
    depths = [int(line.strip()) for line in fin.readlines()]

print(sonar_sweep(group_by_n(depths, 3)))
