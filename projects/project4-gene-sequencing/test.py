
from typing import Union
# Used to compute the bandwidth for banded version
MAXINDELS = 3

# Used to implement Needleman-Wunsch scoring
MATCH = -3
INDEL = 5
SUB = 1

word1 = "-other"
word2 = "-thars"

class Node:
    def __init__(self, val, letter=None, parent=None, finished=0) -> None:
        self.value = val
        self.parent = parent
        self.type = None
        self.finished = finished
        self.letter = letter
    
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
    
    new_node = Node(min_val.value, parent=min_val)

    matrix[cur_row][cur_col] = new_node

    if type(min_val) == Node:
        if min_val == up:
            new_node.parent = up
            new_node.type = "delete"
            new_node.letter = "-"
            if add == 0:
                new_node.value -= 3
            else:
                new_node.value += 5
            
        elif min_val == upper_left:
            new_node.parent = upper_left
            new_node.type = "replace"
            new_node.letter = word1[cur_col]
            if add == 0:
                new_node.value -= 3
            else:
                new_node.value += 1

        elif min_val == left:
            new_node.parent = left
            new_node.type = "insert"
            new_node.letter = word1[cur_col]
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

def modify_string(matrix):
    mod_string = list(word1)

    cur_idx = len(mod_string) - 1
    start = matrix[len(word2) - 1][len(word1) - 1]


    while start.parent.letter != None and cur_idx >= 0:
        mod_string[cur_idx] = start.letter
        start = start.parent
        cur_idx -= 1
    
    print(mod_string)



matrix = [[None for itm in word1] for itm in word2]


fill_matrix(matrix, 0, 0)

modify_string(matrix)

printm(matrix)


