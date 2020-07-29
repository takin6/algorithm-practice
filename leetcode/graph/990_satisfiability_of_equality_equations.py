from typing import List
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # graph = [ [] for _ in range(26) ]

        # for eqn in equations:
        #     if eqn[1] == '=':
        #         x = ord(eqn[0]) - ord('a')
        #         y = ord(eqn[3]) - ord('a')

        #         graph[x].append(y)
        #         graph[y].append(x)


        # color = [None] * 26
        # def dfs(node, group):
        #     if color[node] == group: return
        #     color[node] = group

        #     for nei in graph[node]:
        #         dfs(nei, group)

        # group = 0
        # for s in range(26):
        #     if color[s] is None:
        #         dfs(s, group)
        #         group += 1

        # for eqn in equations:
        #     if eqn[1] == '!':
        #         x = ord(eqn[0]) - ord('a')
        #         y = ord(eqn[3]) - ord('a')

        #         if color[x] == color[y]:
        #             return False

        # return True

        import string
        if not equations: return True
        parent = {i:i for i in string.ascii_lowercase}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx

        checks = []
        for eq in equations:
            if eq[1] == '!':
                checks.append(eq)
                continue
            union(eq[0], eq[3])
        
        for chk in checks:
            if find(chk[0]) == find(chk[3]):
                return False
        return True
        
        

# print(Solution().equationsPossible(["a==b","b!=a"]))
print(Solution().equationsPossible(["a==b","e==c","b==c","a!=e"]))