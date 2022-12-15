from advent_lib.advent_lib import *

caloriesList = read_input()
elves = [0]
for line in caloriesList:
    print(line)
    if line == "":
        elves.append(0)
        continue
    elves[-1] += int(line)

print("most calories :", max(elves))
print("top 3 :", sum(sorted(elves)[-3:]))
