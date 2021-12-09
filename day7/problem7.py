# Day 7
# I need a variable that increments and subtracts from the list in the file
# I then need to get the sum of every iteration of each increment
# Lastly, I need to find the lowest sum from all the iterations

f = open('input.txt', 'r')
content = f.read()
lines = list(map(int, content.split(',')))


def get_fuel(position, l):
    fuel = 0
    for line in l:
        fuel += abs(line - position)
    return fuel


def part2(position, l):
    fuel = 0
    for line in l:
        fuel += sum(list(range(abs(line - position)+1)))
    return fuel


print(min([get_fuel(i, lines) for i in range(len(lines))]))
print(min([part2(i, lines) for i in range(len(lines))]))
