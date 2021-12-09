lines = open('input.txt').read().splitlines()
xy_cords = []


def direction(x):
    return (x > 0) - (x < 0)


def count(list, include_diagonals):
    test = {}
    for (x1, y1), (x2, y2) in list:
        if x1 == x2 or y1 == y2 or include_diagonals:
            x_incrament, y_incrament = direction(x2 - x1), direction(y2 - y1)
            while (x1, y1) != (x2 + x_incrament, y2 + y_incrament):
                test[(x1, y1)] = test.get((x1, y1), 0) + 1
                x1 += x_incrament
                y1 += y_incrament
    return sum(x > 1 for x in test.values())


for line in lines:
    first, second = line.split(' -> ')
    x1, y1 = map(int, first.split(','))
    x2, y2 = map(int, second.split(','))
    xy_cords.append(((x1, y1), (x2, y2)))
#print(xy_cords)

print(f'Part 1: {count(xy_cords,False)}, Part 2: {count(xy_cords, True)}')
