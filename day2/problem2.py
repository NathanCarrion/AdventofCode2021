f = open("input.txt", "r") #opens file
content = f.read()
content_list = content.splitlines() #splits lines of the file
content_list = content.split() #seperates the directions and numbers into its own elements on the list
f.close()

first = content_list[1::2] #takes the element from every odd index starting at index=1 (all the numbers)
direction = content_list[::2] #takes the element from every even index starting at index=0 (all the directions)

nums = []
for x in first:
    nums.append(int(x)) #makes the string numbers into int numbers


depth_total = []
aim = 0
horizontal = 0
depth = 0
for i in range(0, len(direction)):
    if direction[i]=="forward":
        horizontal = horizontal + nums[i]
        depth = aim * nums[i]
        depth_total.append(depth) #stores all the different depth values
#        print(f"you have gone {horizontal} horizontally, and your depth ({aim} * {nums[i]}) = {depth}")
    elif direction[i] =="down":
        aim = aim + nums[i]
#        print(f"your aim is {aim} after going down")
    elif direction[i] =="up":
        aim = aim - nums[i]
#        print(f"your aim is {aim} after going up")

multiplied = horizontal * aim 
print(f"the end result for part 1: {multiplied}")
print("the end result for part 2:", end = " ")
print(sum(depth_total) * horizontal)

