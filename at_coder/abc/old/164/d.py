# S = input()
# res = 0

# for i in range(3, len(S)):
#   last = S[i]
#   for j in range(i-3):
#     product = int(S[j:i+1])

#     if product % 2019 == 0:
#       print(product)
#       res += 1

# print(res)


# S = input()
# res = 0

# for i in range(len(S)-1):

#   for j in range(k)
#   last = S[i]
#   for j in range(i-3):
#     product = int(S[j:i+1])

#     if product % 2019 == 0:
#       print(product)
#       res += 1

# print(res)

# S = input()
# cnt = [0] * 10
# N = len(S)

# ans = 0
# cnt[0] = 1
# tot = 0
# p = 1

# for i in range(N)[::-1]:
#   import pdb; pdb.set_trace()
#   tot = (tot + int(S[i]) * p) % 2019

#   ans += cnt[tot]

#   p = (p*10) % 2019
#   cnt[tot] += 1

# print(ans)

# # S = input()
# S = "1817181712114"
# N = len(S)
# ans = 0
# x = 1
# # 累積和を格納
# tot = 0
# # 累積和のmod 2019をカウントする
# cnt = [0] * 2019

# for i in range(N)[::-1]:
#   cnt[tot] += 1

#   tot += int(S[i]) * x
#   tot %= 2019
#   ans += cnt[tot]
#   x *= 10

# print(ans)

from collections import Counter
S = input()[::-1]
MOD = 2019
X = [0]
for i, s in enumerate(S):
  X.append((X[-1] + int(s)*pow(10,i,MOD)) % MOD)

C = Counter(X)
res = 0
for v in C.values():
  res += v*(v-1) // 2

print(res)
print(X)
print(C)

# https://codeforces.com/blog/entry/76539?#comment-611841