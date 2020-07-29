A,B,C,X,Y = map(int,input().split())

res = 10**15
for i in range(0, max(X,Y)*2+1, 2):
  res = min(res, A*max(0,X-i//2)+B*max(0,Y-i//2)+C*i)

print(res)
