N = int(input())
q = []
for i in input():
  if i=="J":
    q.append(0)
  elif i=="O":
    q.append(1)
  else:
    q.appned(2)

# dp[i][j] = i日目に部分集合Sが出席する場合の数
dp = [ [0]*8 for _ in range(N+1) ]
last = 0

for i in range(N):
  for j in range(1<<3):
    if (j>>q[i])&1:
      for k in range(1<<3):
        if (k&j):
          dp[i+1][j]
