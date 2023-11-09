
from typing import Union
# Used to compute the bandwidth for banded version
MAXINDELS = 3

# Used to implement Needleman-Wunsch scoring
MATCH = -3
INDEL = 5
SUB = 1

word1 = "-polynomial"
word2 = "-exponential"

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
                new_node.value += MATCH
            else:
                new_node.value += INDEL
            
        elif min_val == upper_left:
            new_node.parent = upper_left
            new_node.type = "replace"
            new_node.letter = word1[cur_col]
            if add == 0 and not (cur_col == 0 and cur_row == 0):
                new_node.value += MATCH
            elif add == 1 and not (cur_col == 0 and cur_row == 0):
                new_node.value += SUB

        elif min_val == left:
            new_node.parent = left
            new_node.type = "insert"
            new_node.letter = word1[cur_col]
            if add == 0:
                new_node.value -= MATCH
            else:
                new_node.value += INDEL


    if cur_col != len(matrix[0]) - 1:
        fill_matrix(matrix, cur_row, cur_col + 1)

    if cur_col == 0 and cur_row != len(matrix) - 1:
        fill_matrix(matrix, cur_row + 1, cur_col)

def fill_matrix2(matrix):
    for slot in range(len(matrix)):
        matrix[slot][0] = slot
    for slot in range(len(matrix[0])):
        matrix[0][slot] = slot
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            matrix[row][col] = \
            min((MATCH if word1[col] == word2[row] else SUB) + matrix[row - 1][col - 1],
                INDEL + matrix[row][col - 1],
                INDEL + matrix[row - 1][col]
                )


def printm(matrix):
    for row in matrix:
        for col in row:
            print((col.value, col.type[:1]), end=" ")
        print()

def printm2(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end=" ")
        print()

def modify_string(matrix):
    mod_string = list(word1)

    cur_idx = len(mod_string) - 1
    start = matrix[len(word2) - 1][len(word1) - 1]

    cur_indel = 0
    while start.parent.letter != None:
        if start.type == "delete" or start.type == "insert":
            cur_indel += 1
        if cur_indel < MAXINDELS:
            print("TOO MANY INDELS")
            return
        mod_string[cur_idx] = start.letter
        start = start.parent
    
    print(mod_string)


matrix = [[None for itm in word1] for itm in word2]


# fill_matrix(matrix, 0, 0)


# modify_string(matrix)


fill_matrix2(matrix)
printm2(matrix)


