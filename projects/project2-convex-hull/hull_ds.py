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
        self.size = 1



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


def merge(left_hull: Hull, right_hull: Hull):
        
    l_node = left_hull.rightmost
    r_node = right_hull.leftmost

    if left_hull.size == 1 and right_hull.size == 1:
        l_node.cw = r_node
        l_node.ccw = r_node
        r_node.ccw = l_node
        r_node.cw = l_node
        left_hull.rightmost = right_hull.rightmost
        left_hull.size += right_hull.size

        return left_hull
        
    
    cur_slope = get_slope(l_node.value, r_node.value)

    while get_slope(l_node.ccw.value, r_node.value) < cur_slope:
        # Worst case here: checking every right node against every left node.
        # So, for each node on the left (worst case n/2 nodes) I have to check against 
        # each side on the right, making this a total of (n/2) * (n/2) => n^2 work.
        l_node = l_node.ccw
        cur_slope = get_slope(l_node.value, r_node.value)
        while get_slope(l_node.value, r_node.cw.value) > cur_slope:
            r_node = r_node.cw
            cur_slope = get_slope(l_node.value, r_node.value)

    while get_slope(l_node.value, r_node.cw.value) > cur_slope:
        # n^2 work.
        r_node = r_node.cw
        cur_slope = get_slope(l_node.value, r_node.value)
        while get_slope(l_node.ccw.value, r_node.value) < cur_slope:
            l_node = l_node.ccw
            cur_slope = get_slope(l_node.value, r_node.value)

    # upper tangent found, now make the left node cw r_node and right node ccw l node.
    left_top_tangent = l_node
    right_top_tangent = r_node

    # Reset l_node and r_node to begin looking for lower tangent
    l_node = left_hull.rightmost
    r_node = right_hull.leftmost
    
    cur_slope = get_slope(l_node.value, r_node.value)

    while get_slope(l_node.cw.value, r_node.value) > cur_slope:
        # n^2 work
        l_node = l_node.cw
        cur_slope = get_slope(l_node.value, r_node.value)
        while get_slope(l_node.value, r_node.ccw.value) < cur_slope:
            r_node = r_node.ccw
            cur_slope = get_slope(l_node.value, r_node.value)

    while get_slope(l_node.value, r_node.ccw.value) < cur_slope:
        # n^2 work
        r_node = r_node.ccw
        cur_slope = get_slope(l_node.value, r_node.value)
        while get_slope(l_node.cw.value, r_node.value) > cur_slope:
            l_node = l_node.cw
            cur_slope = get_slope(l_node.value, r_node.value)

    right_top_tangent.ccw = left_top_tangent
    left_top_tangent.cw = right_top_tangent
    l_node.ccw = r_node
    r_node.cw = l_node

    left_hull.rightmost = right_hull.rightmost
    left_hull.size += right_hull.size

    # Total time: 4 * n^2 => n^2

    return left_hull



# Overall the divide and conquer mixed with the merge:
# a = 2
# b = 2
# d = 2
# work to combine = n^2
# Master theorem: 2T(n/2) + O(n^2)
# So, 2/(2^2) = 1/4 < 1, thus the time it takes to do this is O(n^2)