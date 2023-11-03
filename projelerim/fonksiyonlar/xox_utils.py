def draw_grid(grid):
    for row in grid:
        for i, s in enumerate(row):
            if s == 0:
                s = " "
                print(s, end='')
            elif s == 1:
                s = "x"
                print(s, end='')
            else:
                s = "o"
                print(s, end='')

            if i == 2:
                print()
            else:
                print('|', end='')


def update_grid(grid, row, col, is_x):
    if is_x:
        grid[row][col] = 1
    else:
        grid[row][col] = 2

    return grid


def check_row_win(grid, is_x):
    if is_x:
        search_int = 1
    else:
        search_int = 2

    for row in grid:
        if row.count(search_int) == 3:
            return True

    return False


def get_col(grid, col_num):
    col_list = []
    for row in grid:
        element = row[col_num]
        col_list.append(element)
    return col_list


def check_col_win(grid, is_x):
    if is_x:
        search_int = 1
    else:
        search_int = 2

    for i in range(3):
        col = get_col(grid, i)
        if col.count(search_int) == 3:
            return True

    return False


def is_game_over_with_draw(grid):
    for row in grid:
        if row.count(0) > 0:
            return False
    return True


def check_if_won(grid):
    if check_row_win(grid, True):  # x satırdan kazandı mı?
        return 0
    if check_col_win(grid, True):  # x sütundan kazandı mı?
        return 0
    if check_row_win(grid, False):  # o satırdan kazandı mı?
        return 1
    if check_col_win(grid, False):  # 0 sütundan kazandı mı?
        return 1
    if is_game_over_with_draw(grid):  # oyun berabere mi bitmiş?
        return 2
    return 3