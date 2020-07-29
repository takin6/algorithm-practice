S = input()
T = input()
res = "UNRESTORABLE"

for i in range(len(S)-1, len(T)-2, -1):

  s = list(S[::])
  j = i
  flag = True
  for k in range(len(T)-1, -1, -1):
    if s[j] == "?":
      s[j] = T[k]
      j -= 1
    elif s[j] == T[k]:
      j -= 1
      continue
    elif s[j] != T[k]:
      flag = False
      break

  if flag:
    for j in range(len(s)):
      if s[j] == "?": s[j] = "a"
    res = "".join(s)
    break

print(res)

# edge case
# S = "atcoder" T = "atcoder"