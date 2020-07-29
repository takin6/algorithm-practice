from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, curmin, curmax = nums[0],nums[0], nums[0]

        for i in range(1, len(nums)):
            tmp = curmin
            curmin = min(nums[i], curmin*nums[i], curmax*nums[i])
            curmax = max(nums[i], curmax*nums[i], tmp*nums[i])

            if curmax > res:
                res = curmax

        return res

print(Solution().maxProduct([2,3,-2,4]))