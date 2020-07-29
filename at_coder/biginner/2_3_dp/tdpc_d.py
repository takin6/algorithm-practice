import collections 
N,D = map(int, input().split())
prime_factor = collections.defaultdict(int)
for x in [2,3,5]:
  while D%x==0:
    prime_factor[x] += 1
    D //= x
if D>1:
  print(0)
  exit()

f2,f3,f5 = prime_factor[2],prime_factor[3],prime_factor[5]
dp = [ collections.defaultdict(int) for _ in range(N+1) ]
dp[0][(0,0,0)] = 1

factors = [(0,0,0),(1,0,0),(0,1,0),(2,0,0),(0,0,1),(1,1,0)]
for i in range(1, N+1):
  for (a,b,c),count in dp[i-1].items():
    for d2,d3,d5 in factors:
      dp[i][(min(a+d2,f2),min(b+d3,f3),min(c+d5,f5))] += count

print(dp)
print(dp[-1][(f2,f3,f5)] / (6**N))