from xox_utils import draw_grid, update_grid, check_if_won

grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
draw_grid(grid)
ctr = 0

while True:
    if ctr % 2 == 0:
        player_num = 1
    else:
        player_num = 2

    user_input = input('player ' + str(player_num) + ':')
    row_num, col_num = int(user_input.split(',')[0]), int(user_input.split(',')[1])

    if row_num < 0 or row_num > 2:
        print('invalid input!')
        break

    if col_num < 0 or col_num > 2:
        print('invalid input!')
        break

    grid = update_grid(grid, row_num, col_num, player_num == 1)
    draw_grid(grid)
    state = check_if_won(grid)
    if state == 0:
        print('player 1 won!')
        break
    if state == 1:
        print('player 0 won!')
        break
    if state == 2:
        print('draw!')
        break
    ctr += 1
