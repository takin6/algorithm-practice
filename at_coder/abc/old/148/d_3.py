N = int(input())
A = list(map(int,input().split()))

cnt = 0
cur = 1
for i in A:
  if i == cur:
    cur += 1
  else:
    cnt += 1

if cnt == N:
  print(-1)
else:
  print(cnt)