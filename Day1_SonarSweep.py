def sonar_sweep(depths):
    return len([d for idx, d in enumerate(depths) if idx > 0 and d > depths[idx - 1]])


with open("depths_input.txt") as fin:
    depths = [int(line.strip()) for line in fin.readlines()]

print(sonar_sweep(depths))
