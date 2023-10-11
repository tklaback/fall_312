#!/usr/bin/python3


from CS312Graph import *
import time
from heap import Array


class NetworkRoutingSolver:
    def __init__( self):
        pass

    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network

    def getShortestPath( self, destIndex ):
        self.dest = destIndex
        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE
        path_edges = []
        total_length = 0
        node = self.network.nodes[self.source]
        edges_left = 3
        while edges_left > 0:
            edge = node.neighbors[2]
            path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
            total_length += edge.length
            node = edge.dest
            edges_left -= 1
        return {'cost':total_length, 'path':path_edges}

    def computeShortestPaths( self, srcIndex, use_heap=False ):
        self.source = srcIndex
        t1 = time.time()
        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)

        if not use_heap:
            array_pq = Array()
            array_pq.make_queue(self.network, srcIndex)

            u: CS312GraphNode = array_pq.delete_min()
            while array_pq.size != 0 and array_pq.get_dist(u) != float('inf'):
                for each_edge in u.neighbors:
                    if array_pq.get_dist(each_edge.dest) > array_pq.get_dist(each_edge.src) + each_edge.length:
                        array_pq.set_dist(each_edge.dest, array_pq.get_dist(each_edge.src) + each_edge.length)
                        array_pq.set_prev(each_edge.dest, each_edge.src)
                
                u = array_pq.delete_min()
        t2 = time.time()
        return (t2-t1)

