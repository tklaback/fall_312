
from typing import Union
# Used to compute the bandwidth for banded version
MAXINDELS = 3

# Used to implement Needleman-Wunsch scoring
MATCH = -3
INDEL = 5
SUB = 1

word1 = "-exponential"
word2 = "-polynomial"

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
    
def sort_vals(upper_left: Node, up: Node, left: Node, add: int) -> Node:

    # Temporarily add scores to see if there are any ties
    # when finished sorting, set them back
    upper_left.value += MATCH if not add else SUB
    up.value += INDEL
    left.value += INDEL

    min_val = sorted([upper_left, left, up])[0]

    upper_left.value -= MATCH if not add else SUB
    up.value -= INDEL
    left.value -= INDEL

    return min_val


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

    min_val = sort_vals(upper_left, up, left, add)

    new_node = Node(min_val.value, parent=min_val)

    matrix[cur_row][cur_col] = new_node

    if type(min_val) == Node:
        if min_val == up:
            new_node.parent = up
            new_node.type = "delete"
            new_node.letter = ("-", word2[cur_row])
            if add == 0:
                new_node.value += MATCH
            else:
                new_node.value += INDEL
            
        elif min_val == upper_left:
            new_node.parent = upper_left
            new_node.type = "replace"
            new_node.letter = (word1[cur_col], word2[cur_row])
            if add == 0 and not (cur_col == 0 and cur_row == 0):
                new_node.value += MATCH
            elif add == 1 and not (cur_col == 0 and cur_row == 0):
                new_node.value += SUB

        elif min_val == left:
            new_node.parent = left
            new_node.type = "insert"
            new_node.letter = (word1[cur_col], "-")
            if add == 0:
                new_node.value += MATCH
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
            
def fill_matrix2_banded(matrix):
    cur_indel = 0
    matrix[0][0] = (0, None, None)
    for slot in range(1, min(len(matrix) - 1, MAXINDELS) + 1):
        matrix[slot][0] = (INDEL + matrix[slot - 1][0][0], "de", 2)
    for slot in range(1, min(len(matrix[0]) - 1, MAXINDELS) + 1):
        matrix[0][slot] = (INDEL + matrix[0][slot - 1][0], "in", 1)
    for row in range(1, len(matrix)):
        for col in range(max(1, row - MAXINDELS), min(len(matrix[0]) - 1, row + MAXINDELS) + 1):

            final_val = \
            sorted([((MATCH if word1[col] == word2[row] else SUB) + matrix[row - 1][col - 1][0], "diag", 3),
                (INDEL + matrix[row][col - 1][0] if matrix[row][col - 1] else float('inf'), "in", 1),
                (INDEL + matrix[row - 1][col][0] if matrix[row - 1][col] else float('inf'), "de", 2)],
                key=lambda x : (x[0], x[2])
                )[0]

            matrix[row][col] = final_val


def printm(matrix):
    max_width = max(len(f"({col.value}, {col.type[:1]})") for row in matrix for col in row)
    
    for row in matrix:
        for col in row:
            element = f"({col.value}, {col.type[:1]})"
            padding = " " * (max_width - len(element))
            print(f"{element}{padding}", end=" ")
        print()

def printm2(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end=" ")
        print()

def modify_string(matrix):

    mod_string = []


    word2_itr = len(word2) - 1
    word1_itr = len(word1) - 1


    while word1_itr > 0 or word2_itr > 0:
        mod_type = matrix[word2_itr][word1_itr].type
        if mod_type == "replace":

            # mod_string[word1_itr] = word2[word2_itr]
            mod_string.append(matrix[word2_itr][word1_itr].letter)
            word2_itr -= 1
            word1_itr -= 1
        elif mod_type == "insert":
            mod_string.append(matrix[word2_itr][word1_itr].letter)
            word1_itr -= 1
        else:
            mod_string.append("-")
            word2_itr -= 1

    mod_string.reverse()
    
    print(mod_string)


def modify_string_banded(matrix):
    mod_string1 = []
    mod_string2 = []

    word2_itr = len(word2) - 1
    word1_itr = len(word1) - 1

    indel_count = 0
    invalid = False
    while word1_itr > 0 or word2_itr > 0:
        if abs(indel_count) > MAXINDELS:
            invalid = True
            break
        mod_type = matrix[word2_itr][word1_itr].type

        mod_string1.append(matrix[word2_itr][word1_itr].letter[0])
        mod_string2.append(matrix[word2_itr][word1_itr].letter[1])
        if mod_type == "replace":
            word2_itr -= 1
            word1_itr -= 1
        elif mod_type == "insert":
            indel_count += 1
            word1_itr -= 1
        else:
            indel_count -= 1
            word2_itr -= 1
    
    if not invalid:
        mod_string1.reverse()
        mod_string2.reverse()
        
        print(mod_string1)
        print(mod_string2)
    else:
        print("INVALID STRING")


matrix = [[None for _ in word1] for itm in word2]


# fill_matrix(matrix, 0, 0)
# modify_string(matrix)

# fill_matrix2(matrix)
# printm2(matrix)
# printm(matrix)

# modify_string_banded(matrix)




fill_matrix2_banded(matrix)
printm2(matrix)

# When breaking ties, make sure to take into account what will be added to the number that you 
# are drawing from: 

# 5 1
# 1 

# So, here if indel is +5 and it is not a match (so replace is +1),
# then upper_left, top and left will all yield the same result

