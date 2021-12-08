def unique_digit_count(outputs):
    unique_lengths = [2, 3, 4, 7]
    return sum(
        [
            len([len(ele) for ele in outlist if len(ele) in unique_lengths])
            for outlist in outputs
        ]
    )


def decode_inputs(inputs):
    positions_dict = {}
    decode_dict = {}
    input_sets = [set(inp) for inp in inputs]
    for s in input_sets:
        if len(s) == 7:
            decode_dict[8] = s
        elif len(s) == 4:
            decode_dict[4] = s
        elif len(s) == 3:
            decode_dict[7] = s
        elif len(s) == 2:
            decode_dict[1] = s

    positions_dict['top'] = decode_dict[7] - decode_dict[1]
    positions_dict['topleft'] = decode_dict[4] - decode_dict[1]
    positions_dict['middle'] = decode_dict[4] - decode_dict[1]
    positions_dict['topright'] = decode_dict[7].intersection(decode_dict[1])
    positions_dict['bottomright'] = decode_dict[7].intersection(decode_dict[1])
    for s in input_sets:
        if len(s) == 5 and positions_dict['topright'].issubset(s):
            decode_dict[3] = s
        if len(s) == 6 and not(positions_dict['topright'].issubset(s)):
            decode_dict[6] = s

    positions_dict['topleft'] = decode_dict[4] - decode_dict[3]
    positions_dict['middle'] = positions_dict['middle'] - \
        positions_dict["topleft"]
    positions_dict['bottomright'] = decode_dict[6].intersection(decode_dict[1])
    positions_dict['topright'] = positions_dict['topright'] - \
        positions_dict['bottomright']
    for s in input_sets:
        if len(s) == 6 and s != decode_dict[6]:
            if positions_dict['middle'].issubset(s):
                decode_dict[9] = s
            else:
                decode_dict[0] = s
        if len(s) == 5:
            if positions_dict['topright'] not in s:
                decode_dict[5] = s
            if positions_dict['bottomright'] not in s:
                decode_dict[2] = s
    print(positions_dict)
    print(decode_dict, sorted(decode_dict.keys()))


with open("segments.txt") as fin:
    output_data = [
        line.strip().split("|")[1][1:].split(" ") for line in fin.readlines()
    ]

with open("segments.txt") as fin:
    dacta_dict = {
        tuple(line.strip().split("|")[1][1:].split(" ")): line.strip()
        .split("|")[1][1:]
        .split(" ")
        for line in fin.readlines()
    }

single_input_test = [
    "acedgfb",
    "cdfbe",
    "gcdfa",
    "fbcad",
    "dab",
    "cefabd",
    "cdfgeb",
    "eafb",
    "cagedb",
    "ab",
]

single_output_test = ["cdfeb", "fcadb", "cdfeb", "cdbaf"]

num_segments_dict = {0: 6, 1: 2, 2: 5, 3: 5,
                     4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

print(decode_inputs(single_input_test))

# print(unique_digit_count(output_data))
