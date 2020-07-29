from collections import defaultdict,deque
from typing import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [ [] for _ in range(numCourses) ]
        for u,v in prerequisites:
            adj_list[u].append(v)
        # -1: being visited
        #  1: done visited
        visited = [0] * numCourses

        def dfs(n):
            if visited[n] == -1: return False
            if visited[n] == 1: return True
            
            visited[n] = -1
            for nei in adj_list[n]:
                if not dfs(nei):
                    return False
            visited[n] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                print(visited)
                return False
        return True

# print(Solution().canFinish(2, [[1,0]]))
# print(Solution().canFinish(2, [[1,0], [0,1]]))
# print(Solution().canFinish(3, [[1,0], [2,1]]))
print(Solution().canFinish(2, [[0,1]]))