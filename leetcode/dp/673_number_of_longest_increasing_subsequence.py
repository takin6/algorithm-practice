'''
[2,6,3,4, ...]

state:
  - number of lis ending at i (cnt[i])
  - the length of list ending at i (dp[i])

base case: number of list ending at 0
cnt[0] = 1
dp[0] = 1
for all i: cnt[i] = 1

transition / recurrence:
if nums[j] < nums[i]:
  cnt[i] = cnt[j] + 1
  dp[i] = 

 
'''

class Solution:
    def findNumberOfLIS(self, nums):
        N = len(nums)
        if N <= 1: return N
        length, counts = [0] * N, [1] * N

        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]:
                    if length[i] >= length[j]:
                        length[j] = 1 + length[i]
                        counts[j] = counts[i]
                    elif length[i] + 1:
                        counts[j] += counts[i]

        longest = max(length)
        return sum(c for i,c in enumerate(counts) if length[i] == longest)

# print(Solution().findNumberOfLIS([1,3,5,4,7]))
# print(Solution().findNumberOfLIS([2,2,2,2,2]))
print(Solution().findNumberOfLIS([1,2,3,1,2,3,1,2,3]))