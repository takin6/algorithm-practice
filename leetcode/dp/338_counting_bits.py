from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
      dp = [0] * (num+1)
      # offset = 1

      # for i in range(1, num+1):
      #   if offset * 2 == i:
      #     offset *= 2

      #   dp[i] = dp[i-offset] + 1

      # return dp

      for i in range(1, num+1):
        # even
        if i&1 == 0:
          import pdb; pdb.set_trace()
          dp[i] = dp[i>>1]
        else:
          dp[i] = dp[i-1] + 1

      return dp


print(Solution().countBits(5))