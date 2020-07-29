INF = 10 ** 18

# k = 3
# h = [10, 30, 40, 50, 20]

# dp = [INF] * len(h)

# def chmin(i, new):
#   if dp[i] > new:
#     dp[i] = new
#     return True
#   return False

# def chmax(i, new):
#   if dp[i] < new:
#     dp[i] = new
#     return True
#   return False

# dp[0] = 0

# for i in range(1, len(h)):
#   for j in range(1, k+1):
#     if i >= j:
#       chmin(i, dp[i-j] + abs(h[i] - h[i-j]))

# print(dp)
# print(dp[-1])


INF = 10 ** 18
n, k = map(int, input().split())
h = list(map(int, input().split()))

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

dp[0] = 0


# --------  もらうDPの場合 ---------------
# for i in range(1, len(h)):
#   for j in range(1, k+1):
#     if i >= j:
#       chmin(i, dp[i-j] + abs(h[i] - h[i-j]))


# --------  配るDPの場合 ----------------
for i in range(0, n):
  for j in range(1, k+1):
    # import pdb; pdb.set_trace()
    chmin(i+j, dp[i] + abs(h[i] - h[i + j]))

print(dp[-1])