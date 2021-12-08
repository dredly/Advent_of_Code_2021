def unique_digit_count(outputs):
    unique_lengths = [2, 3, 4, 7]
    return sum(
        [
            len([len(ele) for ele in outlist if len(ele) in unique_lengths])
            for outlist in outputs
        ]
    )


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

num_segments_dict = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

# print(unique_digit_count(output_data))
