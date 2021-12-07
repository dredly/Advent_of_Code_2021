import itertools

test_list = [[1], [2], [3, 4], [5]]

flattened = list(itertools.chain(*test_list))

print(flattened, len(flattened))
