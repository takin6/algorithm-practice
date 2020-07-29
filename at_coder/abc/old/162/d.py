# N = int(input())
# S = input()

# # これをn^2にするやり方を自力で考えてみる
# # keyword: 実験！！！！
# res = 0
# for i in range(N):
#   for j in range(i+1, N):
#     for k in range(j+1, N):
#       if (j-i) != (k-j):
#         if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
#           res += 1

# print(res)

N = int(input())
S = input()

# 方針：r, g, bのすべての組み合わせから、j-i=k-jを引く

r, g, b = 0, 0, 0
for c in S:
  if c == "R": r += 1
  if c == "G": g += 1
  if c == "B": b += 1

total = r*g*b

for i in range(N):
  for j in range(i+1, N):
    if S[i] == S[j]: continue

    k = 2*j - i
    if k >= N: continue
    if S[i] == S[k] or S[j] == S[k]: continue
    total -= 1

print(total)

