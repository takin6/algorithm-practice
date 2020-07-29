import bisect
N = int(input())
SPANS = []

for _ in range(N):
  a,b = map(int, input().split())
  SPANS.append([a-b,a+b])

SPANS = sorted(SPANS, key=lambda x: (-x[0], -x[1]))

dp = [SPANS[0][1]]
for i in range(1, len(SPANS)):
  _,r = SPANS[i]
  if r > dp[-1]:
    dp.append(r)
  else:
    dp[bisect.bisect_left(dp, r)] = r

print(len(dp))

# dp = [SPANS[0]]

# for i in range(1, len(SPANS)):
#   l,r = SPANS[i]
#   ll,rr = SPANS[-1]
#   if l < ll and r > rr:
#     dp.append((l,r))
#   else:
#     idx = bisect.bisect_left([x for x,y in dp], l)
#     if idx

# print(SPANS)