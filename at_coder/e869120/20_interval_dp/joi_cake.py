# N = int(input())
# A = []
# for _ in range(N):
#   A.append(int(input()))

# dp = [ [0]*N for _ in range(N) ]
# for i in range(N):
#   dp[i][i] = A[i]

# for l in range(1,N):
#   for i in range(N):
#     j = (i+l)%N

#     if (i*2+l) % 2 == 0:
#       dp[i][j] = max(A[i]+dp[(i+1)%N][j], dp[i][(j-1)%N]+A[j])
#     else:
#       if A[i] > A[j]:
#         dp[i][j] = dp[(i+1)%N][j]
#       else:
#         dp[i][j] = dp[i][(j-1)%N]
#       # dp[i][j] = min(dp[(i+1)%N][j], dp[i][(j-1)%N])

# res = 0
# for d in dp:
#   res = max(res, max(d))

# print(res)

# for d in dp: print(d)


# import sys
# input=sys.stdin.readline
 
# n = int(input())
# a = [int(input()) for i in range(n)]
 
# dp = [[0]*n for i in range(n)]
# for i in range(n):
#   for L in range(n):
#     R = (L+i)%n
#     print(L,R)
#     if (n-(i+1))%2 == 1:
#       # IOI
#       print("IOI",L,R)
#       dp[L][R] = dp[(L+1)%n][R] if a[L] > a[R] else dp[L][(R-1)%n]
#     else:
#       # JOI
#       print("JOI",L,R)
#       dp[L][R] = max(dp[(L+1)%n][R]+a[L], dp[L][(R-1)%n]+a[R])

# for d in dp: print(d)
# ans = 0
# for i in range(n):
#     ans = max(ans, dp[i][i-1])
# print(ans)


import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
 
N = int(input())
U = 2 * N + 1
 
A = [int(input()) for _ in range(N)]
A = A + A
 
dp = [[0] * U for _ in range(U)]
for d in range(1, N + 1):
    for l in range(U - d):
        if N % 2 != d % 2:  # IOIちゃん
            if A[l] > A[l + d - 1]:
                dp[l][l+d] = dp[l+1][l+d]
            else:
                dp[l][l + d] = dp[l][l+d-1]
        else:  # JOIくん
            dp[l][l+d] = max(A[l] + dp[l+1][l+d], A[l+d-1] + dp[l][l+d-1])
 
ans = 0
for l in range(N+1):
    ans = max(ans, dp[l][l + N])
print(ans)

for d in dp: print(d)