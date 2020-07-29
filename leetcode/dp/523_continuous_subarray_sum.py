from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}
        cumsum = 0

        for i, num in enumerate(nums):
            cumsum += num

            if k != 0:
                cumsum = cumsum % k

            if cumsum == 0:
                return True

            if cumsum in dic:
                if i - dic[cumsum] > 1: return True
            else:
                dic[cumsum] = i

        return False

print(Solution().checkSubarraySum([23,2,4,6,7], -6))
print(Solution().checkSubarraySum([23,2,6,4,7], 6))