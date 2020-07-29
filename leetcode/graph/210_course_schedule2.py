from typing import List
from collections import defaultdict
class Solution:
    def __init__(self):
        self.has_cycle = False

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        WHITE, GRAY, BLACK = 0, 1, 2

        visited = [False] * numCourses
        stack = []
        colors = [0] * numCourses

        adj_list = [ [] for _ in range(numCourses) ]
        for c, dep in prerequisites:
            adj_list[c].append(dep)

        def topologicalSort(n):
            visited[n] = True
            colors[n] = GRAY

            for neighbor in adj_list[n]:
                if colors[neighbor] == GRAY:
                    self.has_cycle = True
                    return
                if visited[neighbor] == False and self.has_cycle == False:
                    topologicalSort(neighbor)

            colors[n] = BLACK
            stack.append(n)

        for n in range(numCourses):
            if visited[n] == False:
                topologicalSort(n)

        return [] if self.has_cycle else stack

print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(Solution().findOrder(2, [[1, 0]]))
print(Solution().findOrder(2, [[0, 1]]))

print(Solution().findOrder(2, [[0, 1], [1, 0]]))
