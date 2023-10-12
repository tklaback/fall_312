from typing import Dict, List, Tuple

from CS312Graph import CS312GraphNode

class Heap:

    def get_parent(self, vert: CS312GraphNode) -> CS312GraphNode:
        pass

    def get_length(self, vert: CS312GraphNode) -> float:
        pass
    
    def get_dist(self, node: CS312GraphNode) -> int:
        pass
    
    def set_dist(self, node: CS312GraphNode, dist: int) -> None:
        pass
    
    def set_prev(self, node: CS312GraphNode, prev: CS312GraphNode) -> None:
        pass

    def decrease_key(self, vert: CS312GraphNode) -> None:
        pass


class Array(Heap):
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
        cur_min = float('inf')
        final_node = None
        for node in self._node_to_priority:
            if self._node_to_priority[node][0] < cur_min and not self._node_to_priority[node][1]:
                final_node = node
                cur_min = self._node_to_priority[node][0]

        if final_node == None:
            return
        self._node_to_priority[final_node][1] = True
        self.size -= 1

        return final_node


    def get_dist(self, node: CS312GraphNode) -> int:
        return self._node_to_priority[node][0]
    
    def set_dist(self, node: CS312GraphNode, dist: int) -> None:
        self._node_to_priority[node][0] = dist
    
    def set_prev(self, node: CS312GraphNode, prev: CS312GraphNode) -> None:
        self._node_to_priority[node][2] = prev

    def get_q(self) -> Dict[CS312GraphNode, Tuple[int, bool, CS312GraphNode]]:
        return self._node_to_priority
    
            
    def get_parent(self, vert: CS312GraphNode) -> CS312GraphNode:
        return_vert: CS312GraphNode = self._node_to_priority.get(vert, None)
        if return_vert:
            return return_vert[2]
    
    def get_length(self, vert: CS312GraphNode) -> float:
        return self._node_to_priority[vert][0]

class BinaryHeap(Heap):

    def __init__(self) -> None:
        self._node_to_priority: Dict[CS312GraphNode, int] = {} # Mapping cs312Nodes to their respective priorities
        self._pointer_array: Dict[CS312GraphNode, int] = {} # Mapping cs312nodes to their respective indices in heap
        self._heap: List[CS312GraphNode] = []
        self._prev: Dict[CS312GraphNode, CS312GraphNode] = {} # Maps node to previous node

    def make_queue(self, arr: List[CS312GraphNode], start_node: CS312GraphNode) -> None:
        self._heap.append(start_node)
        self._prev[start_node] = None
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
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self._node_to_priority[self._heap[parent_idx]] > self._node_to_priority[self._heap[cur_idx]]:
                
                self._heap[cur_idx], self._heap[parent_idx] = \
                self._heap[parent_idx], self._heap[cur_idx]

                # must change array pos at each swap
                self._pointer_array[self._heap[cur_idx]] = cur_idx
                self._pointer_array[self._heap[parent_idx]] = parent_idx 

            cur_idx = parent_idx
        

    def delete_min(self) -> CS312GraphNode:
        if len(self._heap):
            return_node = self._heap[0]
            new_node: CS312GraphNode = self._heap.pop()
            if len(self._heap):
                self._heap[0] = new_node
                self._pointer_array[new_node] = 0
                self._perc_down(0)
            return return_node
    
    def _perc_down(self, cur_idx: int) -> None:
        while 2 * cur_idx + 1 < len(self._heap):
            small_side: int = self._get_min_child(cur_idx)

            if self._node_to_priority[self._heap[cur_idx]] > self._node_to_priority[self._heap[small_side]]:
                self._heap[cur_idx], self._heap[small_side] = \
                self._heap[small_side], self._heap[cur_idx]

                # must change array pos at each swap
                self._pointer_array[self._heap[cur_idx]] = cur_idx
                self._pointer_array[self._heap[small_side]] = small_side 
            
            else:
                break

            cur_idx = small_side


    def decrease_key(self, vert: CS312GraphNode) -> None:
        cur_idx = self._pointer_array[vert]
        self._perc_up(cur_idx)

    def _get_min_child(self, cur_idx: int) -> int:
        if 2 * cur_idx + 2 > len(self._heap) - 1:
            return 2 * cur_idx + 1
        if self._node_to_priority[self._heap[2 * cur_idx + 2]] > self._node_to_priority[self._heap[2 * cur_idx + 1]]:
            return 2 * cur_idx + 1
        return 2 * cur_idx + 2
    
    
    def get_parent(self, vert: CS312GraphNode) -> CS312GraphNode:
        return self._prev.get(vert, None)
    
    def get_length(self, vert: CS312GraphNode) -> float:
        return self._node_to_priority[vert]
    
    def get_dist(self, node: CS312GraphNode) -> int:
        return self._node_to_priority[node]
    
    def set_dist(self, node: CS312GraphNode, dist: int) -> None:
        self._node_to_priority[node] = dist

    def set_prev(self, node: CS312GraphNode, prev: CS312GraphNode) -> None:
        self._prev[node] = prev