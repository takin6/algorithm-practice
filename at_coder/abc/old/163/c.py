# 自分より社員番号が小さい直属の上司がちょうど 1人

# 社員番号 iの社員の直属の上司の社員番号が Ai
N = int(input())
A = list(map(int, input().split()))

res = [0] * N
for a in A:
  res[a-1] += 1

for i in res:
  print(i)
