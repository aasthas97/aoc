import string

f = open('input.txt', 'r')
input = f.read().split("\n")
priority_score = 0

for rucksack in input:
    items_in_compartment = int(len(rucksack) / 2)
    compartment_one  = set(rucksack[:items_in_compartment])
    compartment_two = set(rucksack[items_in_compartment:])
    common_item = list(compartment_one.intersection(compartment_two))[0]
    if common_item.islower():
        priority_score += string.ascii_lowercase.index(common_item) + 1
    else:
        priority_score += string.ascii_uppercase.index(common_item) + 27

print(priority_score)
