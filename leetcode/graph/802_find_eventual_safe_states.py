from typing import List

# 0: have not been visited
# 1: safe
# 2: unsafe

import collections
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # not visited, on process, has been processed
        WHITE, GRAY, BLACK = 0, 1, 2
        color = collections.defaultdict(int)

        def dfs(node):
            print("first", node)
            if color[node] != WHITE:
                return color[node] == BLACK

            color[node] = GRAY
            for nei in graph[node]:
                print("nei", nei)
                if color[nei] == BLACK:
                    continue
                # if cycle is detected
                if color[nei] == GRAY or not dfs(nei):
                    return False

            print("second", node)
            color[node] = BLACK
            print(color)

            return True

        return filter(dfs, range(len(graph)))


print(Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))