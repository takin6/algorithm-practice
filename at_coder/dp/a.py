
# template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return 1; } return 0; }
# template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return 1; } return 0; }
INF = 10 ** 18

h = [10, 30, 40, 20] # 30
# h = [30, 10, 60, 10, 60, 50] # 40
dp = [INF] * len(h)

def chmin(i, new):
  if dp[i] > new:
    dp[i] = new
    return True
  return False

def chmax(i, new):
  if dp[i] < new:
    dp[i] = new
    return True
  return False

# ----------------- non-recursive solution  -----------------
# dp[0] = 0

# for i in range(1, len(h)):
#   chmin(i, dp[i-1] + abs(h[i]-h[i-1]))
#   if i > 1:
#     chmin(i, dp[i-2] + abs(h[i]-h[i-2]))

# print(dp)
# print(dp[-1])


#----------------- recursive solution with dp -----------------
# def rec(i):
#   if dp[i] < INF: return dp[i]
#   if i == 0: 
#     dp[i] = 0
#     return 0

#   chmin(i, rec(i-1) + abs(h[i] - h[i-1]))
#   if i > 1: 
#     # import pdb; pdb.set_trace()
#     chmin(i, rec(i-2) + abs(h[i] - h[i-1]))

#   print(i)
#   print(dp)

#   return dp[i]

# rec(len(h)-1)
# print(dp[-1])


# 