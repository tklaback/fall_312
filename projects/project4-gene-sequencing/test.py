
from typing import Union
# Used to compute the bandwidth for banded version
MAXINDELS = 3

# Used to implement Needleman-Wunsch scoring
MATCH = -3
INDEL = 5
SUB = 1

word1 = "-OTHER"
word2 = "-THARS"

class Node:
    def __init__(self, val, parent=None, finished=0) -> None:
        self.value = val
        self.parent = parent
        self.type = None
        self.finished = finished
    
    def __lt__(self, other: 'Node'):

        priority_dyct = {'insert': 1, 'delete': 2, 'replace': 3}

        if self.value == other.value:
            return priority_dyct.get(self.type, 1) < priority_dyct.get(other.type, 1)

        return self.value < other.value


def fill_matrix(matrix, cur_row, cur_col):

    if cur_col == 0 and cur_row == 0:
        upper_left = Node(0, finished=1)
    elif cur_col == 0 or cur_row == 0: 
        upper_left = Node(float('inf'))
    else:
        upper_left = matrix[cur_row - 1][cur_col - 1]

    left = Node(float('inf')) if cur_col == 0 else matrix[cur_row][cur_col - 1]

    up = Node(float('inf')) if cur_row == 0 else matrix[cur_row - 1][cur_col]

    add = 0 if word1[cur_col] == word2[cur_row] else 1

    min_val = sorted([upper_left, left, up])[0]
    
    new_node = Node(min_val.value, min_val)

    matrix[cur_row][cur_col] = new_node

    if type(min_val) == Node:
        if min_val == up:
            new_node.parent = up
            new_node.type = "delete"
            if add == 0:
                new_node.value -= 3
            else:
                new_node.value += 5
            
        elif min_val == upper_left:
            new_node.parent = upper_left
            new_node.type = "replace"
            if add == 0:
                new_node.value -= 3
            else:
                new_node.value += 1

        elif min_val == left:
            new_node.parent = left
            new_node.type = "insert"
            if add == 0:
                new_node.value -= 3
            else:
                new_node.value += 5


    if cur_col != len(matrix[0]) - 1:
        fill_matrix(matrix, cur_row, cur_col + 1)

    if cur_col == 0 and cur_row != len(matrix) - 1:
        fill_matrix(matrix, cur_row + 1, cur_col)

def printm(matrix):
    for row in matrix:
        for col in row:
            print((col.value, col.type[:1]), end=" ")
        print()

def modify_string(matrix, mod_string, orig_string):
    pass



matrix = [[None for itm in word1] for itm in word2]


fill_matrix(matrix, 0, 0)

modify_string(matrix, word1, word2)

printm(matrix)


