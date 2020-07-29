from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(set)

        for u, v in prerequisites:
            adj_list[u].add(v)

        white, gray, black = set(), set(), set()
        for n in range(numCourses): white.add(n)

        def dfs_has_cycle(current):
            move_vertex(current, white, gray)

            for neighbor in adj_list[current]:
                if neighbor in black: continue
                if neighbor in gray: return True
                if dfs_has_cycle(neighbor) == True:
                    return True

            move_vertex(current, gray, black)

            return False

        def move_vertex(n, source, destination):
            source.remove(n)
            destination.add(n)

        while len(list(white)) > 0:
            current = next(iter(white))
            if dfs_has_cycle(current) == True:
                return False

        return True 

# print(Solution().canFinish(2, [[1,0],[0,1]]))
print(Solution().canFinish(2, [[1,0]]))


# 0 - 1
# 1 - 0

# white = []
# gray = [0, 1]
# black = []