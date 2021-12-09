f=open("input.txt","r")
content = f.read()
content_list = content.split('\n')
bingo_nums = list(map(int,content_list[0].split(',')))
bingo_card = []
empty_card = []
for row in content_list[2:]:
    if row == "":
        bingo_card.append(empty_card)
        empty_card = []
    else:
        empty_card.append(list(map(int, row.split())))
if empty_card:
    bingo_card.append(empty_card)

f.close
#print(f"How many elements in content_list: {len(content_list)}")
#print(f"total amount of playable boards: {len(content_list)/5}")
#print(f"Length of call_order: {len(call_order)}")
#print(bingo_card)
#print(bingo_nums)

def check_rows(card):
    return any(all(x =='X' for x in row) for row in card)

def check_if_win(card):
    transpose = list(map(list, zip(*card)))
    return check_rows(card) or check_rows(transpose)

def check_num(card,x):
    for i, row in enumerate(card):
        for j, k in enumerate(row):
            if k == x:
                card[i][j] = 'X'
    return card

def total_card(card):
    return sum(sum(x for x in row if type(x) == int) for row in card)

def part_one(bingo_nums, bingo_card):
    for num in bingo_nums:
        for i, card in enumerate(bingo_card):
            cur = check_num(card, num)
            if check_if_win(cur):
                return total_card(cur) * num
            bingo_card[i] = cur

def part_two(bingo_nums, bingo_card):
    winners = set()
    for num in bingo_nums:
        for i, card in enumerate(bingo_card):
            if i in winners:
                continue
            cur = check_num(card, num)
            if check_if_win(cur):
                if len(winners) == len(bingo_card) -1:
                    return total_card(cur) * num
                winners.add(i)
            bingo_card[i] = cur

print(f"Part 1: {part_one(bingo_nums, bingo_card)}")
print(f"Part 2: {part_two(bingo_nums, bingo_card)}")
