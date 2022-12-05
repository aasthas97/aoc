"""Advent of Code Day 1.
https://adventofcode.com/2022/day/1
Author: Aastha"""

import re

f = open('input.txt', 'r')
input = f.read().split("\n\n")
max_calories = 0
max_calories_2 = 0
max_calories_3 = 0

for elf in input:
    elf_calories = re.split("\n", elf)
    total_elf_calories = sum([int(cal) for cal in elf_calories if cal != ''])
    # print(total_elf_calories)
    if total_elf_calories > max_calories:
        max_calories = total_elf_calories
    elif total_elf_calories > max_calories_2:
        max_calories_2 = total_elf_calories
    elif total_elf_calories > max_calories_3:
        max_calories_3 = total_elf_calories

print("Calories carried by the top Elf:", max_calories)

### PART TWO
print("Total calories carried by the top three elves: ", max_calories + max_calories_2 + max_calories_3)