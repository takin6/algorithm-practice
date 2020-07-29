# 音声信号: 静数列
# 整数列：一定期間でサンプリングしふり幅を記録
# 差分パルス符号変調: 前後の値の差分を符号化し，圧縮率を向上

# codebook: yn = yn-1+C[kn]
# K(n) = 出力系列
# C[j] = コードブックの値

while True:
  N,M = map(int,input().split())
  if N==M==0: exit()
  sample = []
  for _ in range(M):
    sample.append(int(input()))
  codes = []
  for _ in range(N):
    codes.append(int(input()))

  # dp[i][j] = i番目までのコードで、yがjになるときのときに、(code-y)**2の和の最小値
  INF = float('inf')
  dp = [ [INF]*(256) for _ in range(N+1) ]
  dp[0][128] = 0
  for i in range(N):
    code = codes[i]
    for j in range(256):
      if dp[i][j] < INF:

        for k in range(M):
          y = max(0, min(255, j+sample[k]))
          # import pdb; pdb.set_trace()
          dp[i+1][y] = min(dp[i+1][y], dp[i][j]+(code-y)**2)

  print(min(dp[-1]))
# import pdb; pdb.set_trace()

# INF = -10**6
# dp = [INF] * (M+1)
# dp[0] = 128
# for i in range(M):
#   s = sample[i]
#   for j in range(1,N):
#     code = codes[j]
#     prev_code = codes[j-1]

#     cur = (dp[j]-code)**2 - (dp[j-1]-prev_code)**2
#     new = ((dp[j]+s)-code)**2 - (dp[j-1]-prev_code)**2
#     import pdb; pdb.set_trace()
#     if new < cur:
#       dp[j] = dp[j-1]+s

# print(dp)