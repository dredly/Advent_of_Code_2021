def get_risk_level(heightmap):
    current_sum = 0
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            neighbours = []
            if i - 1 in range(len(heightmap)):
                neighbours.append(heightmap[i - 1][j])
            if j + 1 in range(len(heightmap[i])):
                neighbours.append(heightmap[i][j + 1])
            if i + 1 in range(len(heightmap)):
                neighbours.append(heightmap[i + 1][j])
            if j - 1 in range(len(heightmap[i])):
                neighbours.append(heightmap[i][j - 1])
            if all(n > heightmap[i][j] for n in neighbours):
                current_sum += heightmap[i][j] + 1
    return current_sum


def get_local_minima(heightmap):
    minima_coords = []
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            neighbours = []
            if i - 1 in range(len(heightmap)):
                neighbours.append(heightmap[i - 1][j])
            if j + 1 in range(len(heightmap[i])):
                neighbours.append(heightmap[i][j + 1])
            if i + 1 in range(len(heightmap)):
                neighbours.append(heightmap[i + 1][j])
            if j - 1 in range(len(heightmap[i])):
                neighbours.append(heightmap[i][j - 1])
            if all(n > heightmap[i][j] for n in neighbours):
                minima_coords.append((i, j))
    return minima_coords


with open("smoke_data.txt") as fin:
    smoke_data = [
        [int(digit) for digit in list(line.strip())] for line in fin.readlines()
    ]

print(get_risk_level(smoke_data))
