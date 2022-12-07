import re

with open('input.txt', 'r') as f:
    elvish_work = f.read().split("\n")

part_one = 0
part_two = 0
for elf_pair in elvish_work:
    l1, l2, r1, r2 = [int(x) for x in re.split('[,-]', elf_pair)]
    elf1 = set(range(l1, l2+1))
    elf2 = set(range(r1, r2+1))

    # if (l1 >= r1 and l2 <= r2) or (r1 >= l1 and r2 <= l2):
    #     part_one += 1
    if (elf1.issubset(elf2) or elf2.issubset(elf1)):
        part_one += 1
    if (elf1.intersection(elf2)):
        part_two +=1

print("Part one:", part_one)
print("Part two", part_two)