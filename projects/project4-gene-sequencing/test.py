
from typing import Union
# Used to compute the bandwidth for banded version
MAXINDELS = 3

# Used to implement Needleman-Wunsch scoring
MATCH = -3
INDEL = 5
SUB = 1

word1 = "-ATAFFGT"
word2 = "-ACCGTFF"

class Node:
    def __init__(self, val, parent=None) -> None:
        self.value = val
        self.parent = parent
        self.type = None
    
    def __lt__(self, other: 'Node'):

        priority_dyct = {'insert': 1, 'delete': 2, 'replace': 3}

        if self.value == other.value:
            return priority_dyct.get(self.type, 1) < priority_dyct.get(other.type, 1)

        return self.value < other.value


def fill_matrix(matrix, cur_row, cur_col):

    if cur_col == 0 and cur_row == 0:
        upper_left = Node(0)
    elif cur_col == 0 or cur_row == 0: 
        upper_left = Node(float('inf'))
    else:
        upper_left = matrix[cur_row - 1][cur_col - 1]

    left = Node(float('inf')) if cur_col == 0 else matrix[cur_row][cur_col - 1]

    up = Node(float('inf')) if cur_row == 0 else matrix[cur_row - 1][cur_col]

    add = 0 if word1[cur_col] == word2[cur_row] else 1

    min_val = sorted([upper_left, left, up])[0]
    
    new_node = Node(min_val.value + add, min_val) if type(min_val) == Node else Node(min_val + add, min_val)

    matrix[cur_row][cur_col] = new_node

    if type(min_val) == Node:
        if min_val == up:
            new_node.parent = up
            new_node.type = "delete"
        elif min_val == upper_left:
            new_node.parent = upper_left
            new_node.type = "replace"
        elif min_val == left:
            new_node.parent = left
            new_node.type = "insert"


    if cur_col != len(matrix[0]) - 1:
        fill_matrix(matrix, cur_row, cur_col + 1)

    if cur_col == 0 and cur_row != len(matrix) - 1:
        fill_matrix(matrix, cur_row + 1, cur_col)

def printm(matrix):
    for row in matrix:
        for col in row:
            print(col.value, end=" ")
        print()

def modify_string(matrix, mod_string, orig_string):
    cur_idx = len(mod_string) - 1
    # string1

    target = (len(orig_string) - 1, len(mod_string) - 1)

    start: Node = matrix[target[0]][target[1]]

    my_sting_arr = list(mod_string)
    mod_str_idx = cur_idx
    while start.parent:
        print(start.type)
        if start.type == "delete":
            my_sting_arr[cur_idx] = "-"
        else:
            my_sting_arr[cur_idx] = mod_string[mod_str_idx]
            mod_str_idx -= 1
        cur_idx -= 1
        start = start.parent
    
    print(my_sting_arr)

    print(start)


matrix = [[None for itm in word1] for itm in word2]


fill_matrix(matrix, 0, 0)

modify_string(matrix, word1, word2)

printm(matrix)


