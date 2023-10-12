from typing import Dict, List, Tuple
from CS312Graph import CS312GraphNode

class Heap:

    def decrease_key(self, vert: CS312GraphNode) -> None:
        pass

    def insert(self, vert: CS312GraphNode) -> None:
        pass

    def make_queue(self, arr: List[CS312GraphNode] ) -> 'Heap':
        pass

    def pop(self) -> CS312GraphNode:
        pass


class Array:
    def __init__(self) -> None:
        self._node_to_priority: Dict[CS312GraphNode, Tuple[int, bool, CS312GraphNode]] = {}
        # dictionary maps nodes to their distance, whether they have been visited, and their parent node
        self.cur_min: List[CS312GraphNode, int] = [None, float('inf')]
        self.size: int = 0


    def make_queue(self, arr: List[CS312GraphNode], startNode: CS312GraphNode):

        for node in arr:
            if node == startNode: self._node_to_priority[node] = [0, False, None]
            else: self._node_to_priority[node] = [float('inf'), False, None]
            self.size += 1

    def delete_min(self) -> CS312GraphNode:
        for node in self._node_to_priority:
            if self._node_to_priority[node][0] < self.cur_min[1] and not self._node_to_priority[node][1]:
                self.cur_min = [node, self._node_to_priority[node][0]]

        min_node =  self.cur_min[0]
        if min_node == None:
            return
        self._node_to_priority[min_node][1] = True
        self.size -= 1
        self.cur_min = [None, float("inf")]

        return min_node
    
    # def decrease_key(self, node: CS312GraphNode, new_dist: int) -> None:
    #     self._node_to_priority[node][0] = new_dist

    def get_dist(self, node: CS312GraphNode) -> int:
        return self._node_to_priority[node][0]
    
    def set_dist(self, node: CS312GraphNode, dist: int) -> None:
        self._node_to_priority[node][0] = dist
    
    def set_prev(self, node: CS312GraphNode, prev: CS312GraphNode) -> None:
        self._node_to_priority[node][2] = prev

    def get_q(self) -> Dict[CS312GraphNode, Tuple[int, bool, CS312GraphNode]]:
        return self._node_to_priority


class BinaryHeap(Heap):

    def __init__(self) -> None:
        self._node_to_priority: Dict[str, Tuple[str, bool]] = {}
        self._heap: List[CS312GraphNode] = []

    def make_queue(self, arr: List[CS312GraphNode] ) -> Heap:
        pass



