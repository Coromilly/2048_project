import copy
import random


def pretty_print(massive):
    print('-' * 10)
    for row in massive:
        print(*row)
    print('-' * 10)


def get_number_from_index(row_num, col_num):
    return row_num * 4 + col_num + 1


def get_index_from_number(number):
    number -= 1
    x, y = number // 4, number % 4
    return x, y


def insert_2_or_4(massive, row_num, col_num):
    if random.random() <= 0.75:
        massive[row_num][col_num] = 2
    else:
        massive[row_num][col_num] = 4
    return massive


def get_empty_list(massive):
    empty = []
    for i in range(4):
        for j in range(4):
            if massive[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty


def is_zero_in_mas(massive):
    for row in massive:
        if 0 in row:
            return True
    return False


def move_left(massive):
    origin = copy.deepcopy(massive)
    delta = 0
    for row in massive:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if massive[i][j] == massive[i][j+1] and massive[i][j] != 0:
                massive[i][j] *= 2
                delta += massive[i][j]
                massive[i].pop(j+1)
                massive[i].append(0)
    return massive, delta, not origin == massive


def move_right(massive):
    delta = 0
    origin = copy.deepcopy(massive)
    for row in massive:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for i in range(4):
        for j in range(3, 0, -1):
            if massive[i][j] == massive[i][j-1] and massive[i][j] != 0:
                massive[i][j] *= 2
                delta += massive[i][j]
                massive[i].pop(j-1)
                massive[i].insert(0, 0)
    return massive, delta, not origin == massive


def move_up(massive):
    delta = 0
    origin = copy.deepcopy(massive)
    for j in range(4):
        column = []
        for i in range(4):
            if massive[i][j] != 0:
                column.append(massive[i][j])
        while len(column) != 4:
            column.append(0)
        for i in range(3):
            if column[i] == column[i+1] and column[i] != 0:
                column[i] *= 2
                delta += column[i]
                column.pop(i+1)
                column.append(0)
        for i in range(4):
            massive[i][j] = column[i]

    return massive, delta, not origin == massive


def move_down(massive):
    delta = 0
    origin = copy.deepcopy(massive)
    for j in range(4):
        column = []
        for i in range(4):
            if massive[i][j] != 0:
                column.append(massive[i][j])
        while len(column) != 4:
            column.insert(0, 0)
        for i in range(3, 0, -1):
            if column[i] == column[i-1] and column[i] != 0:
                column[i] *= 2
                delta += column[i]
                column.pop(i-1)
                column.insert(0, 0)
        for i in range(4):
            massive[i][j] = column[i]
    return massive, delta, not origin == massive


def can_move(massive):
    for i in range(3):
        for j in range(3):
            if massive[i][j] == massive[i][j+1] or massive[i][j] == massive[i+1][j]:
                return True
    for i in range(1, 4):
        for j in range(1, 4):
            if massive[i][j] == massive[i-1][j] or massive[i][j] == massive[i][j-1]:
                return True
    return False
