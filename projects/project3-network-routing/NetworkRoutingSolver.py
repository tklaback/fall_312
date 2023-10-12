#!/usr/bin/python3


from CS312Graph import *
import time
from heap import Array


class NetworkRoutingSolver:
    def __init__( self):
        self.array_pq = Array()

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

        print(self.network.getNodes()[destIndex])
        nodes = self.network.getNodes()
        shortest_map = self.array_pq.get_q()

        cur_node = nodes[destIndex]
        total_length = shortest_map[cur_node][0]

        while shortest_map[cur_node][0] != 0:
            prev = shortest_map[cur_node][2]
            for e in prev.neighbors:
                if e.dest == cur_node:
                    edge = e
                    break

            path_edges.append((cur_node.loc, shortest_map[cur_node][2].loc, '{:.0f}'.format(edge.length))) #,' {:.0f}'.format(edge.length)))
            cur_node = shortest_map[cur_node][2] # tuple of int, bool and CS312GraphNode
            
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
            
            self.array_pq.make_queue(self.network.getNodes(), self.network.getNodes()[srcIndex])

            u: CS312GraphNode = self.array_pq.delete_min()
            while u:
                for each_edge in u.neighbors:
                    if self.array_pq.get_dist(each_edge.dest) > self.array_pq.get_dist(each_edge.src) + each_edge.length:
                        self.array_pq.set_dist(each_edge.dest, self.array_pq.get_dist(each_edge.src) + each_edge.length)
                        self.array_pq.set_prev(each_edge.dest, each_edge.src)
                
                u = self.array_pq.delete_min()
        t2 = time.time()
        return (t2-t1)

