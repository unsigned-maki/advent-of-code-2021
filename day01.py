# https://adventofcode.com/2021/day/1
report = open("input").readlines()

previous = 0
increases = 0

for i in report:
    if previous:
        if int(i) > int(previous):
            increases = increases + 1
    previous = i

print(increases)
