N,M = map(int,input().split())
INF = float('inf')
dist = [[INF]*N for _ in range(N)]
times = [[INF]*N for _ in range(N)]
for _ in range(M):
  s,t,d,time = map(int,input().split())
  s -= 1
  t -= 1
  dist[s][t],dist[t][s] = d,d
  times[s][t],times[t][s] = time,time

dp = [ [-1]*N for _ in range(1<<N) ] 
cnt = [ [-1]*N for _ in range(1<<N) ]
def tsp(mask, pos):
  if dp[mask][pos] != -1:
    return dp[mask][pos]

  if mask == (1<<N)-1 and pos==0:
    cnt[mask][pos] = 1
    return 0

  ans = float('inf')
  for i in range(N):
    if mask&(1<<i)==0:
      newAns = dist[pos][i] + tsp(mask|1<<i, i)
      if newAns > times[pos][i]: continue
      if newAns < ans:
        ans = newAns
        cnt[mask][pos] = cnt[mask|1<<i][i]
      else:
        cnt[mask][pos] += cnt[mask|1<<i][i]

  dp[mask][pos] = ans
  return ans

# for c in cnt: print(c)
print(tsp(0,0))
for c in cnt: print(c)
