# n日、m個
# Ai日間
# 遊べる日
N,M = list(map(int, input().split()))
A = list(map(int, input().split()))

if N-sum(A) < 0:
  print(-1)
else:
  print(N - sum(A))
