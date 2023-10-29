

word1 = "-other"
word2 = "-thars"

class Node:
    def __init__(self, val, parent=None) -> None:
        self.value = val
        self.parent = parent
        self.type = None

def fill_matrix(matrix, cur_row, cur_col):

    if cur_col == 0 and cur_row == 0:
        upper_left = 0 
    elif cur_col == 0 or cur_row == 0: 
        upper_left = float('inf')
    else:
        upper_left = matrix[cur_row - 1][cur_col - 1]

    left = float('inf') if cur_col == 0 else matrix[cur_row][cur_col - 1]

    up = float('inf') if cur_row == 0 else matrix[cur_row - 1][cur_col]

    add = 0 if word1[cur_col] == word2[cur_row] else 1

    min_val = sorted([upper_left, left, up], key=lambda x:x.value if type(x) == Node else x)[0]
    
    new_node = Node(min_val.value + add, min_val) if type(min_val) == Node else Node(min_val + add, min_val)

    if type(min_val) == Node:
        if min_val.parent == up:
            new_node.type = "delete"
        elif min_val.parent == upper_left:
            new_node.type = "replace"
        else:
            new_node.type = "insert"

    matrix[cur_row][cur_col] = new_node

    if cur_col != len(matrix[0]) - 1:
        fill_matrix(matrix, cur_row, cur_col + 1)

    if cur_col == 0 and cur_row != len(matrix) - 1:
        fill_matrix(matrix, cur_row + 1, cur_col)




def printm(matrix):
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()



matrix = [[None for itm in word1] for itm in word2]


fill_matrix(matrix, 0, 0)
printm(matrix)



