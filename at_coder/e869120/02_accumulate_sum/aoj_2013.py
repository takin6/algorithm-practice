
# hour-> minute -> second
# 1hour -> 60 minute -> 3600

def to_second(t):
  res = 0
  hour,minute,second = t.split(":")
  res += int(hour)*60*60
  res += int(minute)*60
  res += int(second)
  return res

while True:
  N = int(input())
  if N == 0: exit()
  times = [0] * (24*60*60)
  for _ in range(N):
    s,t = map(str,input().split())
    times[to_second(s)] += 1
    times[to_second(t)] -= 1

  for t in range(24*60*60-1):
    times[t+1] += times[t]

  print(max(times))