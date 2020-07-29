# N = int(input())
# presents = [ list(map(int, input().split())) for _ in range(N) ]

# presents = sorted(presents, key=lambda x: x[0], reverse=True )

# dp = [0] * N
# dp[0] = 1

# for i in range(1, N):

#   longest = 1
#   for j in range(i):
#     if presents[i][0] < presents[j][0] and presents[i][1] < presents[j][1]:
#       longest = max(longest, dp[j]+1)

#   dp[i] = longest

import bisect

N = int(input())
presents = [ list(map(int, input().split())) for _ in range(N) ]
presents = sorted(presents, key=lambda x: (x[0],-x[-1]))
# presents = sorted(presents, key=lambda x: x[0])

LIS = []

for i, (h, w) in enumerate(presents):
    if i == 0:
        LIS.append(w)
 
    elif LIS[-1] < w:
        LIS.append(w)
    else:
        i = bisect.bisect_left(LIS, w)
        LIS[i] = w

print(presents)
print(LIS)
print(len(LIS))


# lambda x: (x[0],x[-1]): sort by x[0] (small->big) then x[1](big->small)
# reason: to prevent the elements with the same height to take
#         small width always
# ex)
# 5
# 2 2
# 2 1
# 8 8
# 5 3
# 4 4

# update the least height greedily
