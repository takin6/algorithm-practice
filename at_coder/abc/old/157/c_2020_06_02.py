N,M = map(int,input().split())
S,C = [],[]
for _ in range(M):
  s,c = map(int,input().split())
  S.append(s)
  C.append(c)


for i in range(1000):
  i = str(i)
  if len(i) != N: continue

  flg = True
  for j in range(M):
    if i[S[j]-1] != str(C[j]):
      flg = False
  if flg:
    print(i)
    exit()

print(-1)
# print(ans)