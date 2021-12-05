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
            if check_for_win(board, numbers[:i+1]):
                winning_board = check_for_win(board, numbers[:i+1])
                winning_board_numbers = [n for row in winning_board for n in row]
                score = sum([n for n in winning_board_numbers if n not in numbers[:i+1]]) * num
                return score

def losing_board_score(numbers, boards):
    for i, num in enumerate(numbers):
        for board in boards:
            if check_for_win(board, numbers[:i+1]):
                winning_board = check_for_win(board, numbers[:i+1])
                winning_board_numbers = [n for row in winning_board for n in row]
                score = sum([n for n in winning_board_numbers if n not in numbers[:i+1]]) * num
                if len(boards) == 1:
                    return score
                else:
                    boards.remove(winning_board)
                    return losing_board_score(numbers, boards)

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
 
print(winning_board_score(numbers, boards))
print(losing_board_score(numbers, boards))