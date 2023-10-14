from typing import Dict, List, Tuple

from CS312Graph import CS312GraphNode
import sys

class Heap:
    def __init__(self) -> None:
        self._prev: Dict[CS312GraphNode, CS312GraphNode] = {} # Maps node to previous node

    def make_queue(self, arr: List[CS312GraphNode], startNode: CS312GraphNode) -> None:
        """Has O(n) time complexity for both implementations"""
        pass

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
        """dictionary maps nodes to their distance, whether they have been visited, and their parent node"""
        super().__init__()
        self._node_to_priority: Dict[CS312GraphNode, int] = {}
        self._node_to_visited: Dict[CS312GraphNode, bool] = {}


    def make_queue(self, arr: List[CS312GraphNode], startNode: CS312GraphNode) -> None:
        for node in arr:
            if node == startNode: 
                self._node_to_priority[node] = 0 
                
            else: 
                self._node_to_priority[node] = float('inf')
            
            self._node_to_visited[node] = False
            self._prev[node] = None

    def delete_min(self) -> CS312GraphNode:
        """Delete min has O(n) time complexity since it must loop through each element to see if it is the min"""
        cur_min = float('inf')
        final_node = None
        for node in self._node_to_priority:
            if self._node_to_priority[node] < cur_min and not self._node_to_visited[node]:
                final_node = node
                cur_min = self._node_to_priority[node]

        if final_node == None:
            return
        self._node_to_visited[final_node] = True

        return final_node


    def get_dist(self, node: CS312GraphNode) -> int:
        """O(1)"""
        return self._node_to_priority[node]
    
    def set_dist(self, node: CS312GraphNode, dist: int) -> None:
        """O(1)"""
        self._node_to_priority[node] = dist
    
    def set_prev(self, node: CS312GraphNode, prev: CS312GraphNode) -> None:
        """O(1)"""
        self._prev[node] = prev
            
    def get_parent(self, vert: CS312GraphNode) -> CS312GraphNode:
        """O(1)"""
        return self._prev.get(vert, None)

    
    def get_length(self, vert: CS312GraphNode) -> float:
        """O(1)"""
        return self._node_to_priority[vert]

class BinaryHeap(Heap):

    def __init__(self) -> None:
        """Maps cs312Nodes to their respective prioriteis and respective indices in the heap"""
        super().__init__()
        self._node_to_priority: Dict[CS312GraphNode, int] = {}
        self._pointer_array: Dict[CS312GraphNode, int] = {}
        self._heap: List[CS312GraphNode] = []
        

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
        """O(_perc_up)"""
        self._heap.append(vert)
        self._perc_up(len(self._heap) - 1)
    
    def _perc_up(self, cur_idx: int) -> None:
        """O(logn) because we move up a tree height of one at each iteration"""
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
        """O(_perc_down)"""
        if len(self._heap):
            return_node = self._heap[0]
            new_node: CS312GraphNode = self._heap.pop()
            if len(self._heap):
                self._heap[0] = new_node
                self._pointer_array[new_node] = 0
                self._perc_down(0)
            return return_node
    
    def _perc_down(self, cur_idx: int) -> None:
        """O(logn) because at eah iteration we are moving down the tree 1 layer (a.k.a moving through array by multiples of two)"""
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
        """O(_perc_up)"""
        cur_idx = self._pointer_array[vert]
        self._perc_up(cur_idx)

    def _get_min_child(self, cur_idx: int) -> int:
        """O(1)"""
        if 2 * cur_idx + 2 > len(self._heap) - 1:
            return 2 * cur_idx + 1
        if self._node_to_priority[self._heap[2 * cur_idx + 2]] > self._node_to_priority[self._heap[2 * cur_idx + 1]]:
            return 2 * cur_idx + 1
        return 2 * cur_idx + 2
    
    
    def get_parent(self, vert: CS312GraphNode) -> CS312GraphNode:
        """O(1)"""
        return self._prev.get(vert, None)
    
    def get_length(self, vert: CS312GraphNode) -> float:
        """O(1)"""
        return self._node_to_priority[vert]
    
    def get_dist(self, node: CS312GraphNode) -> int:
        """O(1)"""
        return self._node_to_priority[node]
    
    def set_dist(self, node: CS312GraphNode, dist: int) -> None:
        """O(1)"""
        self._node_to_priority[node] = dist

    def set_prev(self, node: CS312GraphNode, prev: CS312GraphNode) -> None:
        """O(1)"""
        self._prev[node] = prev