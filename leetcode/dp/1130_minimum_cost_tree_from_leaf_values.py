from typing import List
import math
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # memo = {}
        
        # def dfs(i,j):
        #     if i+1 >= j: return 0

        #     if (i,j) not in memo:
        #         ans = float('inf')
        #         for k in range(i+1, j):
        #             left = dfs(i, k)
        #             right = dfs(k, j)
        #             root = max(arr[i:k]) * max(arr[k:j])
        #             ans = min(ans, left+right+root)
        #         memo[(i,j)] = ans

        #     return memo[(i,j)]

        # return dfs(0, len(arr))

        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            t = min(arr[i - 1:i] + arr[i + 1:i + 2]) * arr.pop(i)
            import pdb; pdb.set_trace()
            print(t)
            res += t
        return res

print(Solution().mctFromLeafValues([6,2,4]))