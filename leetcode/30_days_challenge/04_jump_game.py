from typing import List
class Solution:
    # # backtracking solution
    # def canJump(self, nums: List[int]) -> bool:
    #     self.res = False
    #     self.memo = {}

    #     return self.helper(0, nums)

    # def helper(self, idx, nums):
    #     if idx == len(nums)-1:
    #         return True

    #     furthestJump = min(len(nums)-1, idx+nums[idx])
    #     for i in range(idx+1, furthestJump+1):
    #         if self.helper(i, nums):
    #             return True

    #     return False

    # =================================================
    # memoization solution
    # def canJump(self, nums: List[int]) -> bool:
    #     self.res = False
    #     self.memo = {}
    #     self.memo[len(nums)-1] = True

    #     return self.helper(0, nums)

    # def helper(self, idx, nums):
    #     if self.memo.get(idx) is not None:
    #         return self.memo[idx]

    #     furthestJump = min(len(nums)-1, idx+nums[idx])
    #     for i in range(idx+1, furthestJump+1):
    #         if self.helper(i, nums):
    #             self.memo[i] = True
    #             return True

    #     self.memo[idx] = False
    #     return False


    # ===================================================
    # bottom-up approach
    # def canJump(self,nums: List[int]) -> bool:
    #     UNKNOWN, GOOD, BAD = 2,3,4
    #     memo = [UNKNOWN] * len(nums)
    #     memo[ len(nums)-1 ] = GOOD

    #     for i in reversed(range(0, len(nums)-1)):
    #         print(i)
    #         furthestJump = min(len(nums)-1, i+nums[i])
    #         for j in range(i+1, furthestJump+1):
    #             if memo[j] == GOOD:
    #                 memo[i] = GOOD
    #                 break
    #     return memo[0] == GOOD

    # ===================================================
    # greedy
    def canJump(self, nums):
        lastPos = len(nums)-1
        # for i in reversed(range(len(nums))):
        for i in range(len(nums)-2, -1, -1):
            if i+nums[i] >= lastPos:
                lastPos = i

        return lastPos == 0
        
print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))
print(Solution().canJump([2,0,0]))

