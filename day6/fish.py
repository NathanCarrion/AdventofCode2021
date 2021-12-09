f = open("input.txt", "r")
content = f.read()
fishes = list(map(int, content.split(',')))
f.close()
def growth_list(ages):
    for i in range(len(ages)):
        if ages[i] == 0:
            ages[i] = 6
            ages.append(8)
        else:
            ages[i] -= 1
for i in range(80):
    growth_list(fishes)
print(f"part 1: {len(fishes)}")
########################################################################################################################
f = open("input.txt", "r")
content_list = [int(x) for x in f.read()[:-1].split(',')]
fish = dict()

for age in range(9):
    fish[age] = sum(x == age for x in content_list)


def growth_dic(x):
    baby = x[0]
    for i in range(8):
        if i != 6:
            x[i] = x[i + 1]
        else:
            x[i] = x[i + 1] + baby
    x[8] = baby
    return x


for i in range(256):
    fish = growth_dic(fish)

print(f"Part 2: {sum(fish.values())}")
