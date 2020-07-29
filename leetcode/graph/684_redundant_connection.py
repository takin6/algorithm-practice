from typing import List

import collections
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                print(source, target)
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v

            graph[u].add(v)
            graph[v].add(u)

print(Solution().findRedundantConnection([[1,2], [1,3], [2,3]]))

