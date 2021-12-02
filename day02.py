# https://adventofcode.com/2021/day/2
report = open("input").readlines()

# Part 1

horizontal = 0
depth = 0

for i in report:
    if i[0] == "f":
        horizontal += int(i.replace("forward ", ""))
    elif i[0] == "d":
        depth += int(i.replace("down ", ""))
    elif i[0] == "u":
        depth -= int(i.replace("up ", ""))

print(horizontal * depth)

# Part 2

horizontal = 0
depth = 0
aim = 0

for i in report:
    if i[0] == "f":
        horizontal += int(i.replace("forward ", ""))
        depth += int(i.replace("forward ", "")) * aim
    elif i[0] == "d":
        aim += int(i.replace("down ", ""))
    elif i[0] == "u":
        aim -= int(i.replace("up ", ""))

print(horizontal * depth)
