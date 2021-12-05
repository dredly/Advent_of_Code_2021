import numpy

def check_for_win(board, nums_so_far):
    rows = board
    columns = [list(col) for col in (numpy.transpose(numpy.array(board)))]
    for row in rows:
        if all(num in nums_so_far for num in row):
            return board

    for col in columns:
        if all(num in nums_so_far for num in col):
            return board
    return False

def winning_board_score(numbers, boards):
    for i, num in enumerate(numbers):
        for board in boards:
            check_for_win(board, numbers[:i+1])
            if check_for_win(board, numbers[:i+1]):
                winning_board = check_for_win(board, numbers[:i+1])
                winning_board_numbers = [n for row in winning_board for n in row]
                score = sum([n for n in winning_board_numbers if n not in numbers[:i+1]]) * num
                return score

with open('bingo_input.txt') as fin:
    numbers = [int(n) for n in fin.readlines()[0].split(',')]

with open('bingo_input.txt') as fin:
    board_rows = []
    for line in fin.readlines()[1:]:
        board_row = line.strip().split(' ')
        board_row = [int(n) for n in board_row if n != '']
        board_rows.append(board_row)
    board_rows = [br for br in board_rows if br != []]
    boards = []
    for i in range(0, len(board_rows), 5):
        boards.append(board_rows[i:i+5])
    

test_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
test_boards= [
    [
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 18, 5],
        [1, 12, 20, 15, 19]
    ],
    [
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6]
    ],
    [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7]
    ]
]

print(winning_board_score(test_numbers, test_boards))
print(winning_board_score(numbers, boards))