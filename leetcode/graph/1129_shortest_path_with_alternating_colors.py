import math
from typing import List
from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:

        # RED, BLUE = 0, 1

        # graph = {}

        # # data structure of graph
        # # { starting_node: 
        # #     { 0(red): set(ending_nodes) }, 
        # #       1(blue): set(ending_nodes) },
        # # }
        # for i in range(n): graph[i] = { 0: set(), 1: set() }
        # res = [math.inf] * n

        # for re in red_edges:
        #     f, to = re
        #     graph[f][RED].add(to)

        # for be in blue_edges:
        #     f, to = be
        #     graph[f][BLUE].add(to)

        # q = [ (0, 0), (0, 1) ]
        # level = -1
        # while len(q) > 0:
        #     level += 1
        #     size = len(q)

        #     for _ in range(size):
        #         node, color = q.pop(0)
        #         opp_color = color ^ 1
        #         res[node] = min(level, res[node])
        #         neighbors = graph[node][opp_color]

        #         for neighbor in list(neighbors):
        #             graph[node][opp_color].remove(neighbor)
        #             q.append((neighbor, opp_color))

        # return [ -1 if r == math.inf else r for r in res ]

        RED, BLUE = 1, -1
        adj_list = [ {RED: set(), BLUE: set()} for _ in range(n) ]
        
        for red_edge in red_edges:
            f, t = red_edge
            adj_list[f][RED].add(t)
        for blue_edge in blue_edges:
            f, t = blue_edge
            adj_list[f][BLUE].add(t)
                
        q = [(0, RED), (0, BLUE)]
        step = -1
        res = [math.inf] * n
            
        while q:
            step += 1
            size = len(q)
            
            for _ in range(size):
                node, c = q.pop(0)
                res[node] = min(res[node], step)
                
                opp_c = c * -1
                neighbors = adj_list[node][opp_c]
                for nei in list(neighbors):
                    q.append((nei, opp_c))
                    adj_list[node][opp_c].remove(nei)
                                
        
        return [ -1 if e == math.inf else e for e in res ]

# list
#   - copy of a list uses the same reference
#   - pop() takes a argument position to be poped
#   - stack architecture: first-in-last-out

# set
#   - copy of a set creates another reference
#   - pop takes no argument
#   - queue architecture: first-in-first-out

print(Solution().shortestAlternatingPaths(3, [[0,1],[0,2]], [[1,0]]))
print(Solution().shortestAlternatingPaths(3, [[0, 1]], [[1, 2]]))
