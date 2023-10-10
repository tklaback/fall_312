from PyQt5.QtCore import QPointF
from typing import List

class HullNode:
    def __init__(self, value: QPointF) -> None:
        self.cw: HullNode = self
        self.ccw: HullNode = self
        self.value = value

class Hull:
    def __init__(self, start_node: HullNode) -> None:
        self.rightmost: HullNode = start_node
        self.leftmost: HullNode = start_node

def divide_and_conquer(arr):
    middle = len(arr) // 2

    if len(arr) == 1:
        # constant time
        new_node = HullNode(arr[0])
        new_hull = Hull(new_node)
        return new_hull
    
    left_hull = divide_and_conquer(arr[:middle])
    right_hull = divide_and_conquer(arr[middle:])
    # Dividing the list into 2 each time has logn time complexity

    return merge(left_hull, right_hull)


def get_slope(startCoord: QPointF, endCoord: QPointF):
    return ((endCoord.y() - startCoord.y()) / (endCoord.x() - startCoord.x()))

def get_upper_tangent(l_node: HullNode, r_node: HullNode):
    
    cur_slope = get_slope(l_node.value, r_node.value)
    
    while True:
        modL = False
        modR = False
        while get_slope(l_node.ccw.value, r_node.value) < cur_slope:
            l_node = l_node.ccw
            cur_slope = get_slope(l_node.value, r_node.value)
            modL = True

        while get_slope(l_node.value, r_node.cw.value) > cur_slope:
            r_node = r_node.cw
            cur_slope = get_slope(l_node.value, r_node.value)
            modR = True
        
        if not modR and not modL:
            break

    return l_node, r_node

def get_lower_tangent(l_node: HullNode, r_node: HullNode):
    cur_slope = get_slope(l_node.value, r_node.value)

    while True:
        modR = False
        modL = False
        while get_slope(l_node.cw.value, r_node.value) > cur_slope:
            l_node = l_node.cw
            cur_slope = get_slope(l_node.value, r_node.value)
            modL = True

        while get_slope(l_node.value, r_node.ccw.value) < cur_slope:
            r_node = r_node.ccw
            cur_slope = get_slope(l_node.value, r_node.value)
            modR = True
        
        if not modR and not modL:
            break
    
    return l_node, r_node


def merge(left_hull: Hull, right_hull: Hull):
        
    l_node = left_hull.rightmost
    r_node = right_hull.leftmost
    
    # upper tangent found, now make the left node cw r_node and right node ccw l node.
    left_top_tangent, right_top_tangent = get_upper_tangent(l_node, r_node)

    # Reset l_node and r_node to begin looking for lower tangent

    left_lower_tangent, right_lower_tangent = get_lower_tangent(l_node, r_node)

    #delete the in between nodes
    right_top_tangent.ccw = left_top_tangent
    left_top_tangent.cw = right_top_tangent
    left_lower_tangent.ccw = right_lower_tangent
    right_lower_tangent.cw = left_lower_tangent

    left_hull.rightmost = right_hull.rightmost

    return left_hull


# arr = [QPointF(4, 7), QPointF(5, -4), QPointF(-5, 1), QPointF(-2, 6), QPointF(6, 2), QPointF(0.0, 0.0)]

# hull = divide_and_conquer(sorted(arr, key=lambda x: x.x()))
# pass

# poly.get_convex_hull()


        

