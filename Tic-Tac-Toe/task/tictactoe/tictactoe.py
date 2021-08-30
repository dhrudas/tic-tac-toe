cells = input()

print("-" * 9)
print("|", cells[0], cells[1], cells[2], '|')
print("|", cells[3], cells[4], cells[5], '|')
print("|", cells[6], cells[7], cells[8], '|')
print("-" * 9)


# print(cells)

# for c in cells:
#     print(c)
# cells = input()
# dash = '--' * 3
# m = 0
# print(dash)
# while m < 7:
#     print("| ", end='')
#     for i in range(m, m + 3):
#         print(cells[i], end=' ')
#     print("|")
#     m += 3
# print(dash)

# def create_game_grid(input_):
#     horizontal_line = '---------'
#     vertical_line = '|'
#     area_grid = [input_[0:3], input_[3:6], input_[6:9]]
#     print(horizontal_line)
#     for line in area_grid:
#         print(vertical_line, ' '.join(line), vertical_line)
#     print(horizontal_line)
#
# 
# create_game_grid(cells)
