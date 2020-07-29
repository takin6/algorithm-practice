# money = 300
# item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
# n = len(item)

# for i in range(2**n):
#   bag = []

#   for j in range(n):
#     print(i, j, i>>j, (i>>j)&1)
#     if (i >> j) & 1:
#       bag.append(item[j][0])

#   print(bag)

# S = "125"

# ==== solving using recursion ===========
# S = input()
# N = len(S)

# def helper(i, s):
#   if i == N-1:
#     return sum(list(map(int, s.split("+"))))

#   return helper(i+1, s+S[i+1]) + helper(i+1, s+"+"+S[i+1])

# print(helper(0, S[0]))


# ===== solving using bit traversal =======
S = input()
N = len(S)

sum = 0
for i in range(2**(N-1)):
  pos = 0
  for j in range(N):
    if ((i>>j)&1):
      sum += int(S[pos:j+1])
      pos = j + 1

  sum += int(S[pos:N])

print(sum)
