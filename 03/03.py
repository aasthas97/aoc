def getItemScore(item):
    scores = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
            'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
            'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39,
            'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}
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
