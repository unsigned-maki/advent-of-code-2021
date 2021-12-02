# https://adventofcode.com/2021/day/1
report = open("input").readlines()

# Part 1

previous = 0
increases = 0

for i in report:
    if previous:
        if int(i) > int(previous):
            increases = increases + 1
    previous = i

print(increases)

# Part 2

previous = 0
increases = 0

for i in range(0, len(report)):
    if i + 2 < len(report):
        if previous:
            if int(report[i]) + int(report[i+1]) + int(report[i+2])  > int(previous):
                increases = increases + 1
        previous = int(report[i]) + int(report[i+1]) + int(report[i+2])

print(increases)
