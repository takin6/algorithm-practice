S = input()
N = len(S)
dp = [ [-1]*(N+1) for _ in range(N+1) ]

def rec(l, r):
  print(l,r, S[l:r])
  if r - l <= 2: return 0
  if dp[l][r] != -1: return dp[l][r]

  for m in range(l+1, r):
    # import pdb; pdb.set_trace()
    dp[l][r] = max(dp[l][r], rec(l, m) + rec(m, r))
    if S[l] == "i" and S[m] == 'w' and S[r-1] == "i":
      # if rec(l+1,m) == m-l-1 and rec(m+1, r-1) == r-m-2:
      # import pdb; pdb.set_trace()
      dp[l][r] = r - l

  return dp[l][r]

print(rec(0, N) // 3)