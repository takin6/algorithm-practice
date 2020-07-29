N,K = map(int,input().split())
P = list(map(int,input().split()))
memo = {}

exp = [0]
for p in P:
  exp.append(exp[-1]+(1+p)/2)

res = 0
for i in range(K,N+1):
  res = max(res, exp[i]-exp[i-K])

print(res)
