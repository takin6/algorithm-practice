N = int(input())
# R,B,W,#
matrix = []
for _ in range(5):
  matrix.append(list(input()))

# (r,b,w)
dp = [ [0,0,0] for _ in range(N+1) ]

for i in range(N):
  r,b,w = 0,0,0

  for j in range(5):
    if matrix[j][i] == "R":
      b += 1
      w += 1
    elif matrix[j][i] == "B":
      r += 1
      w += 1
    elif matrix[j][i] == "W":
      r += 1
      b += 1
    else:
      r += 1
      b += 1
      w += 1

  # import pdb; pdb.set_trace()
  dp[i+1][0] = min(dp[i][1]+r, dp[i][2]+r)
  dp[i+1][1] = min(dp[i][0]+b, dp[i][2]+b)
  dp[i+1][2] = min(dp[i][0]+w, dp[i][1]+w)

print(min(dp[-1]))

for d in dp: print(d)