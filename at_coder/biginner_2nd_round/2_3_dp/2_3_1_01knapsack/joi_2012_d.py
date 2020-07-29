D,N = map(int,input().split())
T = []
for _ in range(D):
  T.append(int(input()))
A,B,C = [],[],[]
for _ in range(N):
  a,b,c = map(int,input().split())
  A.append(a)
  B.append(b)
  C.append(c)

dp = [ [0]*(N+1) for _ in range(D+1)]

for d in range(2, D+1):
  for c in range(1, N+1):
    if not A[c-1]<=T[d-1] or not T[d-1]<=B[c-1]: continue

    for pc in range(1, N+1):
      if A[pc-1]<=T[d-2] and T[d-2]<=B[pc-1]:
        dp[d][c] = max(dp[d][c], dp[d-1][pc]+abs(C[c-1]-C[pc-1]))

print(max(dp[-1]))
print(dp)


# dp[d][c] = d日目にcの服を着たときの、最大派手度
# 添え字の扱いがめんどくさすぎる。。。どうにかできないものか
# dpテーブルでの添え字と、実際の添え字を合わせたほうが良い。。
