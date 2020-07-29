# n = int(input())
# strN = str(n)

# ans = 0

# for i in range(1, n):
#   i = str(i)
#   ans += count_pairs(i)

# def count_pairs(i):
#   # 1けた目は、nよりも小さい場合に1を返す
#   if len(i) == 1: 
#     if int(i) < n: return 1
#   else:
#     return


#   # iがnと同じ桁数の場合
#   if len(i) == len(strN):
#     # nの1番目と、iの
#     if not int(strN[0]) <= int(i[-1]): return 0

#     if  


n = int(input())
cnt = [ [0]*10 for _ in range(10)]

for i in range(1, n+1):
  strI = str(i)

  t = strI[0]
  b = strI[-1]
  cnt[int(t)][int(b)] += 1

ans = 0
for j in range(10):
  for k in range(10):
    ans += cnt[j][k] * cnt[k][j]

print(ans)