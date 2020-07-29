from typing import List
import collections

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # reach = [ [False]* n for _ in range(n)]
        # for i in range(n): reach[i][i] = True

        # MAX_INT = 10 ** 10
        # matrix = [ [MAX_INT]*n for _ in range(n) ]

        # for edge in edges:
        #     u, v, w = edge
        #     matrix[u][v], matrix[v][u] = w, w


        # for k in range(n):
        #     for i in range(n):
        #         for j in range(n):
        #             matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        #             if i != j and reach[i][j] == False:
        #               # if i == 0 and j == 2 and k == 1: import pdb; pdb.set_trace()
        #               reach[i][j] = reach[i][j] or matrix[i][j] <= distanceThreshold or (matrix[i][k] + matrix[k][j] <= distanceThreshold)

        # dic = collections.defaultdict(set)
        # for r in range(len(reach)):
        #     trueCount = len([ e for e in reach[r] if e == True ])
        #     dic[trueCount].add(r)

        # return max(list(dic[min(dic.keys())]))

        dis = [[float('inf')] * n for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

        res = { sum(d <= distanceThreshold for d in dis[i]):  i for i in range(n) }
        print(res)
        return res[min(res)]

print(Solution().findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))
print(Solution().findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))

# ---- 
# 0 - (1, 2), (4, 8)
# 1 - (2, 3), (4, 2), (0, 2)
# 2 - (3, 1), (1, 3)
# 3 - (4, 1), (2, 1)
# 4 - (0, 8), (1, 2), (3, 1)

# [ [0, 2, 0, 0, 8],
#   [2, 0, 3, 0, 2],
#   [0, 3, 0, 1, 0],
#   [0, 0, 1, 0, 1],
#   [8, 2, 0, 1, 0]
# ]

# [ [True, False->True, False, False, False], 
#   [False->True, True, False, False, False->True], 
#   [False, False, True, True, True], 
#   [False, False, True, True, True], 
#   [False, False->True, True, True, True] ]