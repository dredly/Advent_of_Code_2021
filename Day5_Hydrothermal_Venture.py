def find_covers_diagonal(line_start, line_end):
    covers = []
    #Vertical line
    if line_start[0] == line_end[0]:
        for num in range(min(line_start[1], line_end[1]), max(line_start[1], line_end[1]) + 1):
            covers.append((line_start[0], num))
    #Horizontal line
    if line_start[1] == line_end[1]:
        for num in range(min(line_start[0], line_end[0]), max(line_start[0], line_end[0]) + 1):
            covers.append((num, line_start[1]))
    #Diagonal line at a 45 degree angle
    if abs(line_end[1] - line_start[1]) == abs(line_end[0] - line_start[0]):
        counter = 0
        if line_start[0] < line_end[0]:
            for num in range(line_start[0], line_end[0] + 1):
                if line_start[1] < line_end[1]:
                    incr = 1
                else:
                    incr = -1
                covers.append((num, line_start[1] + counter))
                counter += incr
        if line_start[0] > line_end[0]:
            for num in range(line_end[0], line_start[0] + 1):
                if line_end[1] < line_start[1]:
                    incr = 1
                else:
                    incr = -1
                covers.append((num, line_end[1] + counter))
                counter += incr
    return covers

def overlaps(line_list):
    covered = []
    for line in line_list:
        covered.extend(find_covers_diagonal(line[0], line[1]))
    overlap_count = [covered.count(coord) for coord in set(covered)]
    num_overlaps = len([ov for ov in overlap_count if ov >= 2])
    return num_overlaps



with open('hydro_data.txt') as fin:
    data_list = [line.strip().split(' -> ') for line in fin.readlines()]
    data_tuple_list = []
    for entry in data_list:
        data_tuple_list.append([tuple(entry[0].split(',')), tuple(entry[1].split(','))])
    line_data = []
    for pair in data_tuple_list:
        start_point = tuple(int(n) for n in pair[0])
        end_point = tuple(int(n) for n in pair[1])
        line_data.append([start_point, end_point])

print(overlaps(line_data))