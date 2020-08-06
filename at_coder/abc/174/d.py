N = int(input())
C = input()

R,W = C.count("R"), C.count("W")

ans = 10**9
# l,r = 仕切りより左側のW, 仕切りより右側のR
l,r = 0,R
for i in range(N+2):
  if 0 < i < N+1: 
    if C[i-1] == "R":
      r -= 1
    else:
      l += 1

  ans = min(ans, max(l,r))

print(ans)





# 8
# WRWWRWRR

# 1



### [l, r) : rは含まない
# N = int(input())
# A = list(map(int,input().split()))
# dp = [ [0]*(N+1) for _ in range(N+1) ]

# # Wは2から
# for W in range(2,N+1): 
#   for i in range(N-W+1): 
#     j = i+W
#     if (W-2)%2==0:
#       if dp[i+1][j-1]==W-2 and abs(A[i]-A[j-1])<=1:
#         dp[i][j] = W
#         continue

#     for k in range(i+1,j):
#       dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j])

# for m in dp: print(m)
# print(dp[0][N])