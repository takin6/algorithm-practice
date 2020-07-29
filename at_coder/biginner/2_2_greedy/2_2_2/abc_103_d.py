N,M = list(map(int, input().split()))
remove = []
for _ in range(M):
  remove.append(list(map(int, input().split())))

remove = sorted(remove, key=lambda x: x[1])

cnt = 1
for i in range(1,M):
  if remove[i-1][1] > remove[i][0]:
    remove[i][1] = remove[i-1][1]
  else:
    cnt += 1

print(cnt)