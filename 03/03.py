from string import ascii_letters

def getItemScore(item):
    scores = {k:j+1 for j, k in enumerate(ascii_letters)}
    return scores[item]

with open('input.txt', 'r') as f:
    elf_input = f.read().split("\n")

priority_sum_one = 0
for rucksack in elf_input:
    items_in_compartment = int(len(rucksack) / 2)
    compartment_one  = set(rucksack[:items_in_compartment])
    compartment_two = set(rucksack[items_in_compartment:])
    common_item = (compartment_one.intersection(compartment_two)).pop()
    priority_sum_one += getItemScore(common_item)

print("Part One:", priority_sum_one)

### PART TWO
priority_sum_two = 0
elf_groups = zip(*[iter(elf_input)]*3)
for group in elf_groups:
    group_set = [set(g) for g in group]
    common_item = (group_set[2].intersection(group_set[0].intersection(group_set[1]))).pop()
    priority_sum_two += getItemScore(common_item)

print("Part Two:", priority_sum_two)