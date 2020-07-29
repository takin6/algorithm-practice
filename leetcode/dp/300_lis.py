from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        N = len(nums)
        for i in range(1,N):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

    def findNumberOfLIS(self, nums: List[int]) -> int:
        from collections import defaultdict
        # dp = [1] * len(nums)
        # N = len(nums)
        # dic = defaultdict(int)
        # dic[1] = len(nums)
        N = len(nums)
        if N <= 1: return N
        # length of LIS ends with nums[i]
        lengths = [1] * N
        # # of LIS which ends with nums[i]
        counts = [1] * N

        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j]:
                    # length[i] = max(length[j]+1, length[i]) 
                    # but we need to compute count also
                    if lengths[i] == lengths[j]:
                        lengths[i] = lengths[j]+1
                        counts[i]  = counts[j]
                    elif lengths[i] == lengths[j]+1:
                        counts[i] += counts[j]

        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)

# print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution().findNumberOfLIS([1,3,5,4,7]))
# print(Solution().findNumberOfLIS([2,2,2,2,2]))
# print(Solution().findNumberOfLIS([1,2,4,3,5,4,7,2]))