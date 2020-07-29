N,K,M = map(int,input().split())
strs = []
for _ in range(N):
  strs.append(input())

l,r = (M-1)*K, M*K-1

for s in strs[l:min(N,r+1)]: print(s)