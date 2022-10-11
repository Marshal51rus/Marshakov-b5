from random import randrange

def fprint(field):
    print('  0 1 2')
    for i in range(N):
        print(i, ' '.join(field[i]))


def user_input():
    user_cross = []
    while True:
        user_cross = list(map(int, list(input("Ваш ход, поставьте крестик, формат (строка колонка): ").split())))
        if len(user_cross) == 2 and all(list(map(lambda x: x in range(N), user_cross))):
            row, col = user_cross[0], user_cross[1]
            if empty_cell(row, col):
                print("Ваш выбор: ", user_cross)
                return user_cross
            else:
                print("Ячейка уже занята, попробуй еще")
        else:
            print("Ваш ввод не распознан, попробуй еще")


def empty_cell(row, col):
    cell = field[row][col]
    if (cell == '-'):
        return True
    else:
        return False


def count_empty_cells():
    count = 0
    for row in field:
        for cell in row:
            if cell == '-':
                count += 1
    return count


def set_zero():
    val = randrange(0, count_empty_cells())

    for row in range(N):
        for col in range(N):
            if val > 0:
                if empty_cell(row, col):
                    val -= 1
            else:
                if empty_cell(row, col):
                    field[row][col] = 'O'
                    return


def check_row(row, sym):
    count = 0
    for col in range(N):
        val = field[row][col]
        if (val == sym):
            count += 1

    return count == 3


def check_col(col, sym):
    count = 0
    for row in range(N):
        val = field[row][col]
        if (val == sym):
            count += 1

    return count == 3


def check_diag1(sym):
    count = 0
    for i in range(N):
        val = field[i][i]
        if (val == sym):
            count += 1

    return count == 3


def check_diag2(sym):
    count = 0
    for i in range(N):
        val = field[i][N - i - 1]
        if (val == sym):
            count += 1

    return count == 3


def check_win(sym):
    check = []

    for i in range(N):
        check.append(check_row(i, sym))
        check.append(check_col(i, sym))

    check.append(check_diag1(sym))
    check.append(check_diag2(sym))

    return any(check)


N = 3
field = [['-' for i in range(N)] for j in range(N)]


while count_empty_cells() > 0:
    fprint(field)
    user_cross = user_input()
    row, col = user_cross[0], user_cross[1]
    field[row][col] = 'X'
    if check_win('X'):
        fprint(field)
        print("Поздравляю, вы выиграли")
        break

    if (count_empty_cells() > 0):
        set_zero()
    if check_win('O'):
        fprint(field)
        print("Поздравляю, вы проиграли")
        break

print("Конец игры")