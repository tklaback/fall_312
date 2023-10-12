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
        self.size: int = 0


    def make_queue(self, arr: List[CS312GraphNode], startNode: CS312GraphNode):

        for node in arr:
            if node == startNode: self._node_to_priority[node] = [0, False, None]
            else: self._node_to_priority[node] = [float('inf'), False, None]
            self.size += 1

    def delete_min(self) -> CS312GraphNode:
        cur_min: List[CS312GraphNode, int] = [None, float('inf')]
        for node in self._node_to_priority:
            if self._node_to_priority[node][0] < cur_min[1] and not self._node_to_priority[node][1]:
                cur_min = [node, self._node_to_priority[node][0]]

        min_node =  cur_min[0]
        if min_node == None:
            return
        self._node_to_priority[min_node][1] = True
        self.size -= 1
        cur_min = [None, float("inf")]

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
        self._node_to_priority: Dict[CS312GraphNode, int] = {} # Mapping cs312Nodes to their respective priorities
        self._pointer_array: Dict[CS312GraphNode, int] = {} # Mapping cs312nodes to their respective indices in heap
        self._heap: List[CS312GraphNode] = []

    def make_queue(self, arr: List[CS312GraphNode], start_node: CS312GraphNode) -> None:
        self._heap.append(start_node)
        self._pointer_array[start_node] = 0
        for itm in arr:
            if itm == start_node:
                self._node_to_priority[itm] = 0
            else:
                self._heap.append(itm)
                self._pointer_array[itm] = len(self._heap) - 1
                self._node_to_priority[itm] = float('inf')


    def insert(self, vert: CS312GraphNode) -> None:
        self._heap.append(vert)
        self._perc_up(len(self._heap) - 1)
    
    def _perc_up(self, cur_idx: int) -> None:
        while (cur_idx - 1) >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self._node_to_priority[self._heap[parent_idx]] > self._node_to_priority[self._heap[cur_idx]]:
                self._heap[cur_idx], self._heap[parent_idx] = \
                self._heap[parent_idx], self._heap[cur_idx]

            cur_idx = parent_idx
        

    def delete_min(self) -> CS312GraphNode:
        return_node = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._perc_down(0)
        return return_node
    
    def _perc_down(self, cur_idx: int) -> None:
        while 2 * cur_idx + 1 < len(self._heap):
            small_side: int = self._get_min_child(cur_idx)

            if self._node_to_priority[self._heap[cur_idx]] > self._node_to_priority[self._heap[small_side]]:
                self._heap[cur_idx], self._heap[small_side] = self._heap[small_side], self._heap[cur_idx]
            else:
                break

            cur_idx = small_side

    def decrease_key(self, vert: CS312GraphNode, new_key: int) -> None:
        self._node_to_priority[vert] = new_key
        cur_idx = self._pointer_array[vert]
        self._perc_up(cur_idx)

    def _get_min_child(self, cur_idx: int) -> int:
        if 2 * cur_idx + 2 > len(self._heap) - 1:
            return 2 * cur_idx + 1
        if self._heap[2 * cur_idx + 2] > self._heap[2 * cur_idx + 1]:
            return 2 * cur_idx + 1
        return 2 * cur_idx + 2