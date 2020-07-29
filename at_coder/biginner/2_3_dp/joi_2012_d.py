D, N = map(int, input().split())
T = [ int(input()) for _ in range(D) ]
A, B, C = [], [], []
for _ in range(N):
  a,b,c = map(int, input().split())
  A.append(a)
  B.append(b)
  C.append(c)

maximum, minimum = [0]*(D+1), [0]*(D+1)
for i in range(D):
  cans = [ C[j] for j,(a,b) in enumerate(zip(A,B)) if a<=T[i]<=b ]
  maximum[i+1], minimum[i+1] = max(cans), min(cans)

dp = [ [0]*2 for _ in range(D+1) ]

for i in range(1, D):
  dp[i+1][0] = max(dp[i][0]+abs(minimum[i+1]-minimum[i]), dp[i][1]+abs(minimum[i+1]-maximum[i])) 
  dp[i+1][1] = max(dp[i][0]+abs(maximum[i+1]-minimum[i]), dp[i][1]+abs(maximum[i+1]-maximum[i])) 

print(max(dp[-1]))