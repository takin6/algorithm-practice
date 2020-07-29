# N個の学期
# 期末テスト1回
# 各学期のscore
# 1 - K-1学期までのscore：つけられない
# K - N学期までのscore：直近K回の期末テストの点数を掛け算

N,K = map(int,input().split())
A = list(map(int,input().split()))

for i in range(K, N):
  if A[i] > A[i-K]:
    print('Yes')
  else:
    print("No")

# for i in range(1,N+1):
#   A[i] = (A[i-1]*A[i])%MOD

# print(A)
# for i in range(K+1, N+1):
#   prev = A[i-1] // A[i-K-1]
#   now = A[i] // A[i-K]
#   if now > prev:
#     print('Yes')
#   else:
#     print("No")