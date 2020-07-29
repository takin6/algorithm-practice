from typing import List
class Solution:
    # def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
    #     # k = 1:
    #     # kadane's algorithm

    #     # k = 2:
    #     # case1. all positive => repeat K times
    #     # case2. all negative => return 0
    #     # case3. positive mixed with negative
    #     #   

    #     maxsum = 0
    #     prev = arr[0]
    #     for i in range(1, len(arr)):
    #         maxsum = max(maxsum, prev+arr[i], arr[i])
    #         prev = max(prev+arr[i], arr[i])

    #     maxsum_of_two = 0
    #     prev = arr[0]
    #     arr += arr
    #     for i in range(1, len(arr)):
    #         maxsum_of_two = max(maxsum_of_two, prev+arr[i], arr[i])
    #         prev = max(prev+arr[i], arr[i])

    #     if k == 1:
    #         return max(0, maxsum) % (10**9+7)
    #     else:
    #         s = sum(arr)
    #         import pdb; pdb.set_trace()
    #         return max(0, (k-2) * max(s, 0) + maxsum_of_two) % (10**9+7)
    # calculate the max sum of subarrays in arr
    # def max_sum(self, arr):
    #     maxsum = max(arr[0], 0)
    #     prev = arr[0]
    #     for i in range(1, len(arr)):
    #         maxsum = max(maxsum, prev+arr[i], arr[i])
    #         prev = max(prev+arr[i], arr[i])

    #     return maxsum
    
    # def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
    #     mod_base = 10 ** 9 + 7
    #     # base cases
    #     if not arr:
    #         return 0
    #     elif k == 1:
    #         return self.max_sum(arr) % mod_base
    #     elif k == 2:
    #         return self.max_sum(arr + arr[::]) % mod_base
        
    #     one = arr
    #     two = arr + arr[::]
    #     three = two + arr[::]
    #     # calculate max sum of subarrays for 0, 1 and 2 repetitions
    #     one_max = self.max_sum(one)
    #     two_max = self.max_sum(two)
    #     three_max = self.max_sum(three)
        
    #     if one_max >= two_max:
    #         return one_max % mod_base
    #     elif two_max >= three_max:
    #         return two_max % mod_base
    #     else:
    #         # this means sum(one) is positive, so we include all the rest of (k - 2) repetitions
    #         return (two_max + (k - 2) * sum(one)) % mod_base

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        def kadane(arr):
            cur, res = 0, 0
            for a in arr:
                cur += a
                if cur < 0:
                    cur = 0
                res = max(res, cur)
            return res

        kadane_v = kadane(arr)
        kadane_v2 = kadane(arr + arr)
        mod = 1000000007
        if k == 1:
            return kadane_v % mod
        
        if sum(arr) > 0:
            return max(sum(arr)*(k-2) + kadane_v2, kadane_v)% mod
        else:
            return max( kadane_v2, kadane_v) % mod
    

# print(Solution().kConcatenationMaxSum([1,-1], 1))

# print(Solution().kConcatenationMaxSum([1,2], 3))
# print(Solution().kConcatenationMaxSum([1,-2,1], 5))
# print(Solution().kConcatenationMaxSum([-1,-2], 7))
# print(Solution().kConcatenationMaxSum([-5,-2,0,0,3,9,-2,-5,4],5))

print(Solution().kConcatenationMaxSum([-2,5,1,-3],3))


