# ====== recursive solution ===========

# s = input()
# n = len(s)

# correct_ops = None
# def helper(cur, i, ops=[]):
#   global correct_ops
#   if i == n and cur == 7: 
#     correct_ops = ops
#     return ops
#   if i == n and cur != 7: return []

#   if helper(cur+int(s[i]), i+1, ops+["+"]): return ops

#   if helper(cur-int(s[i]), i+1, ops+["-"]): return ops

# helper(int(s[0]), 1)

# res = ""
# for i in range(n):
#   if i == n-1:
#     res += s[i]
#   else:
#     res += s[i]+correct_ops[i]

# print(res+"=7")

# ======= bit traverse solution ============
s = input()
n = len(s)

ops = None
for i in range((n-1)**2):
  tmp = int(s[0])
  for j in range(0, n-1):

    if (i>>j)&1:
      tmp += int(s[j+1])
    else:
      tmp -= int(s[j+1])

  if tmp == 7:
    ops = i
    break

res = ""
for i in range(n):
  res += s[i]
  if i < n-1:
    if (ops>>i)&1:
      res += "+"
    else:
      res += "-"

print(res+"=7")



