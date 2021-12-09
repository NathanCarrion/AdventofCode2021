# there are 7 different fields (a - g)
# wires are mixed up randomly so numbers displayed on screen are wrong
# 0 = 6 seg
# 1 = 2 seg unique
# 2 = 5 seg
# 3 = 5 seg
# 4 = 4 seg unique
# 5 = 5 seg
# 6 = 6 seg
# 7 = 3 seg unique
# 8 = 7 seg unique
# 9 = 6 seg


f = open('input.txt', 'r')
lines = f.read().split('|')
f.close()
display_nums = []
for element in lines:
    display_nums.append(element.split())
real_nums = display_nums[1:]
outputs = []

for i in range(len(real_nums)):
    for j in range(0, 4):
        outputs.append(real_nums[i][j])
ones = 0
fours = 0
sevens = 0
eights = 0
for i in range(len(outputs)):
    if len(outputs[i]) == 2:
        ones += 1
    elif len(outputs[i]) == 4:
        fours += 1
    elif len(outputs[i]) == 3:
        sevens += 1
    elif len(outputs[i]) == 7:
        eights += 1

print(f"There are {ones} amount of ones, {fours} amount of fours, {sevens} amount of sevens, {eights} amount of eights")


print(f"Part 1: {ones + fours + sevens + eights}")
#########################################################################################################################

part2 = 0
for f in open('input.txt', 'r'):

    sequence = [set()] * 10
    f = f.split(' | ')
    first = f[0].split(" ")
    # print(first)
    for pattern in first:
        if len(pattern) == 2:  # 1
            sequence[1] = set(pattern)
        elif len(pattern) == 4:  # 4
            sequence[4] = set(pattern)
        elif len(pattern) == 3:  # 7
            sequence[7] = set(pattern)
        elif len(pattern) == 7:  # 8
            sequence[8] = set(pattern)

    for pattern in first:
        if len(pattern) == 6:
            if len(sequence[1] - set(pattern)) == 1:  # 6
                sequence[6] = set(pattern)
    # missing 0, 2, 3, 5, 9
    for pattern in first:
        if len(pattern) == 5:
            if len(sequence[1] - set(pattern)) == 0:
                sequence[3] = set(pattern)
            elif len(set(pattern) - sequence[6]) == 0:
                sequence[5] = set(pattern)
            elif len(set(pattern) - sequence[6]) == 1:
                sequence[2] = set(pattern)

    for pattern in first:
        if len(pattern) == 6 and set(pattern) not in sequence:
            if len(sequence[5] - set(pattern)) == 0:
                sequence[9] = set(pattern)
            else:
                sequence[0] = set(pattern)
    totals = ''
    for i in f[1].split(' '):
        totals += str(sequence.index(set(i.strip())))

    part2 += int(totals)
print(f"Part 2: {part2}")
