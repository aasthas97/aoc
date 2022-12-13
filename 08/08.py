import numpy as np

with open('test-input.txt', 'r') as f:
    elvish_input = f.read().split('\n')

elvish_matrix = np.array([np.array(list(row), dtype=int) for row in elvish_input])
# count trees visible at the edges
visible_trees = (len(elvish_matrix) -2) * 2 + len(elvish_matrix[0]) + len(elvish_matrix[-1])

for i in range(1, len(elvish_matrix)-1):
    for j in range(1, len(elvish_matrix[0])-1):
        tree_height = elvish_matrix[i][j]
        # print(elvish_matrix[i, 0:j+1]) # check row from beginning until tree
        # print(elvish_matrix[i, j:])
        # print(elvish_matrix[0:i+1, j])
        # print(elvish_matrix[i:, j])
        if elvish_matrix[i, 0:j+1].max() == tree_height or elvish_matrix[i, j:].max() == tree_height or elvish_matrix[0:i+1, j].max() == tree_height or elvish_matrix[i:, j].max() == tree_height:
            visible_trees += 1

print(visible_trees)