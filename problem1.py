#reads input.txt file
f = open("input.txt", "r")
content = f.read()
content_list = content.splitlines()
f.close()

#creates a new list with all elements as integers
inputs= []
for x in content_list:
    inputs.append(int(x))

#starts at index 1, takes the first element(i-1) and compares it to the second element(i) to see if second is larger.
#adds 1 to x if second is larger
x = 0
for i in range(1, len(inputs)):
    first = inputs[i-1]
    second = inputs[i]
    if first < second:
        x = x + 1
#answer for part1:
print(f"There are {x} measurements larger than the previous.")

#creates the sliding window of 3 elements in the list inputs and moves over 1 and creates the next window.
part2 = [inputs[x: x + 3] for x in range(0,len(inputs),1)  if x + 3 <= len(inputs)]

#adds the elements of the lists in list "part2" then appends the sums to a new list called "added"
added = []
for j in range(0, len(part2)):
    results = 0
    results = results + sum(part2[j])
    added.append(results)

#same comparison as the first time. 
#adds 1 to y if second is larger.
y = 0
for l in range(1, len(added)):
    first = added[l-1]
    second = added[l]
    if first < second:
        y = y + 1
#answer for part2:
print(f"There are {y} sums larger than the previous sums")
