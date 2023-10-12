#!/usr/bin/python3


from CS312Graph import *
import time
from heap import Array, BinaryHeap


class NetworkRoutingSolver:
    def __init__( self):
        self.pq = None

    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network: CS312Graph = network

    def getShortestPath( self, destIndex ):
        self.dest = destIndex
        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE

    
        path_edges = []

        nodes = self.network.getNodes()
        # shortest_map = self.array_pq.get_q()

        cur_node = nodes[destIndex]
        total_length = self.pq.get_length(cur_node)

        while self.pq.get_parent(cur_node):
            prev = self.pq.get_parent(cur_node)
            for e in prev.neighbors:
                if e.dest == cur_node:
                    edge = e
                    break

            path_edges.append((cur_node.loc, self.pq.get_parent(cur_node).loc, '{:.0f}'.format(edge.length))) #,' {:.0f}'.format(edge.length)))
            cur_node = self.pq.get_parent(cur_node) # tuple of int, bool and CS312GraphNode
            
        # node = self.network.nodes[self.source]
        # edges_left = 3
        # while edges_left > 0:
        #     edge = node.neighbors[2]
        #     path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
        #     total_length += edge.length
        #     node = edge.dest
        #     edges_left -= 1
        return {'cost':total_length, 'path':path_edges}

    def computeShortestPaths( self, srcIndex, use_heap=False ):
        self.source = srcIndex
        t1 = time.time()
        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)

        if not use_heap or use_heap:
            self.pq = Array()
            self.pq.make_queue(self.network.getNodes(), self.network.getNodes()[srcIndex])

            u: CS312GraphNode = self.pq.delete_min()
            while u:
                for each_edge in u.neighbors:
                    if self.pq.get_dist(each_edge.dest) > self.pq.get_dist(each_edge.src) + each_edge.length:
                        self.pq.set_dist(each_edge.dest, self.pq.get_dist(each_edge.src) + each_edge.length)
                        self.pq.set_prev(each_edge.dest, each_edge.src)
                
                u = self.pq.delete_min()
        t2 = time.time()
        return (t2-t1)

