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

    positions_dict["top"] = decode_dict[7] - decode_dict[1]
    positions_dict["topleft"] = decode_dict[4] - decode_dict[1]
    positions_dict["middle"] = decode_dict[4] - decode_dict[1]
    positions_dict["topright"] = decode_dict[7].intersection(decode_dict[1])
    positions_dict["bottomright"] = decode_dict[7].intersection(decode_dict[1])
    for s in input_sets:
        if len(s) == 5 and positions_dict["topright"].issubset(s):
            decode_dict[3] = s
        if len(s) == 6 and not (positions_dict["topright"].issubset(s)):
            decode_dict[6] = s

    positions_dict["topleft"] = decode_dict[4] - decode_dict[3]
    positions_dict["middle"] = positions_dict["middle"] - positions_dict["topleft"]
    positions_dict["bottomright"] = decode_dict[6].intersection(decode_dict[1])
    positions_dict["topright"] = (
        positions_dict["topright"] - positions_dict["bottomright"]
    )
    for s in input_sets:
        if len(s) == 6 and s != decode_dict[6]:
            if positions_dict["middle"].issubset(s):
                decode_dict[9] = s
            else:
                decode_dict[0] = s
        if len(s) == 5:
            if not positions_dict["topright"].issubset(s):
                decode_dict[5] = s
            if not positions_dict["bottomright"].issubset(s):
                decode_dict[2] = s
    return decode_dict


def reverse_lookup(val, input_dict):
    return str(next(k for (k, v) in input_dict.items() if v == val))


def decode_outputs(outputs, decode_dict):
    return int("".join((reverse_lookup(set(outp), decode_dict) for outp in outputs)))


def decode_all(data_dict):
    for inps, outps in list(data_dict.items())[:10]:
        decode_dict = decode_inputs(inps)
        decoded_outputs = decode_inputs(outps, decode_dict)
        print(decoded_outputs)


with open("segments.txt") as fin:
    output_data = [
        line.strip().split("|")[1][1:].split(" ") for line in fin.readlines()
    ]

with open("segments.txt") as fin:
    data_dict = {
        tuple(line.strip().split("|")[0][1:-1].split(" ")): line.strip()
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

# single_output_test = ["cdfeb", "fcadb", "cdfeb", "cdbaf"]

# num_segments_dict = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

# single_decode_dict = decode_inputs(single_input_test)
# print(single_decode_dict)
# print(decode_outputs(single_output_test, single_decode_dict))

# print(unique_digit_count(output_data))

decode_all(data_dict)
