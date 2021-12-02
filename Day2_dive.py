def direction_total(direction, commands):
    return sum((int(c.split(" ")[1]) for c in commands if c.split(" ")[0] == direction))


def final_product(commands):
    return direction_total("forward", commands) * (
        direction_total("down", commands) - direction_total("up", commands)
    )


def new_product(commands):
    aim, depth, position = 0, 0, 0
    for c in commands:
        direction, value = c.split(" ")[0], int(c.split(" ")[1])
        if direction == "forward":
            position += value
            depth += aim * value
        elif direction == "up":
            aim -= value
        elif direction == "down":
            aim += value
    return position * depth


with open("commands.txt") as fin:
    commands = [line.strip() for line in fin.readlines()]

print(final_product(commands))
print(new_product(commands))
