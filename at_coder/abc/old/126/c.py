# dice: 1~N
# coin 
#
# - roll dice, initial_points
# if 1<=points<=K-1:
#       
import math
N,K = map(int,input().split())
res = 0
for i in range(1, N+1):
  k = i
  coin = 0
  while k < K:
    coin += 1
    k *= 2
  res += 1/N * (1/2)**coin
  # print(coin)

print(res)