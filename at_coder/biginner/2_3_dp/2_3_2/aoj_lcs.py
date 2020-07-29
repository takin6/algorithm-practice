# N = int(input())

# for _ in range(N):
#   a = input()
#   b = input()
#   N,M = len(a), len(b)

#   dp = [ [0]*(M+1) for _ in range(N+1)]

#   for i in range(1, N+1):
#     for j in range(1, M+1):
#       if a[i-1] == b[j-1]:
#         dp[i][j] = dp[i-1][j-1]+1
#       else:
#         dp[i][j] = max(dp[i-1][j], dp[i][j-1])

#   print(dp[-1][-1])

# ==== faster answer ===========
# def lcs(X,Y):
#   hist = [0] # yの文字cまでを見た時に, hist[i]以降の文字列において, 共通文字のうち, 一番小さいindexのもの
#   for c in Y:
#     for i in range(len(hist)-1, -1, -1):
#       print(c,i)
#       next_match_i = X.find(c, hist[i])+1
#       if next_match_i:
#         if i+1 < len(hist):
#           hist[i+1] = min(hist[i+1], next_match_i)
#         else:
#           hist.append(next_match_i)
#     print(hist)
#   return len(hist)-1



def lcs(X,Y):
  hist = [0]

  for y in Y:
    for i in range(len(hist)-1, -1, -1):
      found = X.find(y, hist[i])+1
      if found:
        if i+1 >= len(hist):
          hist.append(found)
        else:
          hist[i+1] = min(hist[i+1], found)
  return len(hist)-1


n = int(input())
for _ in range(n):
  a = input()
  b = input()
  print(lcs(a,b))

# print(lcs("abcbdab", "bdcaba"))
# print(lcs("abc","abc"))
# print(lcs("abc","bc"))