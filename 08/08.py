import numpy as np

with open('input.txt', 'r') as f:
    elvish_input = f.read().split('\n')

elvish_matrix = np.array([np.array(list(row), dtype=int) for row in elvish_input])
# count trees visible at the edges
visible_trees = (len(elvish_matrix) -2) * 2 + len(elvish_matrix[0]) + len(elvish_matrix[-1])

for i in range(1, len(elvish_matrix)-1):
    for j in range(1, len(elvish_matrix[0])-1):
        tree_height = elvish_matrix[i][j]
        row_until = elvish_matrix[i, 0:j+1]
        row_after = elvish_matrix[i, j:]
        col_until = elvish_matrix[0:i+1, j]
        col_after = elvish_matrix[i:, j]
        if np.count_nonzero(row_until == tree_height) == 1 and row_until.max() == tree_height:
            visible_trees += 1
        elif np.count_nonzero(row_after == tree_height) == 1 and row_after.max() == tree_height:
            visible_trees += 1
        elif np.count_nonzero(col_until == tree_height) == 1 and col_until.max() == tree_height:
            visible_trees += 1
        elif np.count_nonzero(col_after == tree_height) == 1 and col_after.max() == tree_height:
            visible_trees +=1 
            

print("Number of trees visible:", visible_trees)