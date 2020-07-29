S = input()
N = len(S)
res = 0
for i in range(N):
  if S[i] in "ACGT":
    cnt = 1
    for j in range(i+1, N):
      if S[j] in "ACGT":
        cnt += 1
      else:
        break
    res = max(res, cnt)

print(res)