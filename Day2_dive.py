def direction_total(direction, commands):
    return sum((int(c.split(" ")[1]) for c in commands if c.split(" ")[0] == direction))


def final_product(commands):
    return direction_total("forward", commands) * (
        direction_total("down", commands) - direction_total("up", commands)
    )


with open("commands.txt") as fin:
    commands = [line.strip() for line in fin.readlines()]

print(final_product(commands))
