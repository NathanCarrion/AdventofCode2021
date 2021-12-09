f = open('input.txt', 'r').read().splitlines()
total = 0
h = len(f)  # height
w = len(f[0])  # width
for i in range(h):
    for j in range(w):
        num = f[i][j]
        test = []
        for down_height, down_width in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            next_line = i + down_height
            next_column = j + down_width
            # print(f"this is the down-height{down_height}")
            # print(f"this is the down-width{down_width}")
            if 0 <= next_line < h and 0 <= next_column < w:
                test.append(f[next_line][next_column])
        if all(k > num for k in test):
            total += 1 + int(num)
print(total)

######################################################################################################################
have_seen = [[False] * w for _ in range(w)]


def part2(row, col):
    if not (0 <= row < h and 0 <= col < w):
        return 0
    if have_seen[row][col]:
        return 0
    have_seen[row][col] = True
    if f[row][col] == '9':
        return 0
    output = 1
    for down_row, down_col in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        next_line = row + down_row
        next_column = col + down_col
        if 0 <= next_line < h and 0 <= next_column < w:
            output += part2(next_line, next_column)
    return output


basins = []
for line in range(h):
    for col in range(w):
        basins.append(part2(line, col))
basins.sort()
answer = 1
for x in (basins[-3:]):
    answer *= x
print(answer)
