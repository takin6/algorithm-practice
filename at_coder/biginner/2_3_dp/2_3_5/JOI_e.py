
# dp[i][k] = 最初のi項考えた場合の単調増加な部分列であって、長さがKで
# あるもののうち、その最後の最小値

# import bisect

# def LIS(nums):
#   LIS = [nums[0]]

#   for i in range(1, len(nums)):
#     if nums[i] > LIS[-1]:
#       LIS.append(nums[i])
#     else:
#       LIS[bisect.bisect_left(LIS, nums[i])] = nums[i]

#   print(LIS)
#   return len(LIS)

# print(LIS([10,9,2,5,3,7,101,18]))

# 最初のi項までの単調増加な部分列であって、長さがkであるもののうち最小の値

import bisect
N = int(input())
A = list(map(int,input().split()))
LIS = [ A[0] ]
for i in range(1,N):
  if A[i] > LIS[-1]:
    LIS.append(A[i])
  else:
    LIS[bisect.bisect_left(LIS, A[i])] = A[i]

print(len(LIS))