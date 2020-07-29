## TLE answer ###
# N = int(input())
# dp = [-1] * 394
# dp[0] = 0

# for _ in range(N):
#   s,l,p = map(int,input().split())
  
#   for i in range(1,394):

#     for j in range(s, l+1):
#       if i-j >= 0 and dp[i-j] >= 0:
#         dp[i] = max(dp[i], dp[i-j] + p)


### 長さが違うメロディーを組み合わせれば良い ###
N = int(input())
dp = [-1] * 394
dp[0] = 0

for _ in range(N):
  s,l,p = map(int,input().split())
  for i in range(s, l+1):
    dp[i] = max(dp[i], p)

for i in range(1,394):
  for j in range(i):
    dp[i] = max(dp[i], dp[j]+dp[i-j])

res = []
M = int(input())
for _ in range(M):
  r = dp[int(input())]
  if r == -1:
    print(-1)
    exit()
  else:
    res.append(r)

for r in res: print(r)
