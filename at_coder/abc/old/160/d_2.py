from collections import defaultdict
N,X,Y = map(int,input().split())

counter = defaultdict(int)
for i in range(1,N):
  for j in range(i+1, N+1):
    step = min(j-i, abs(X-i)+1+abs(Y-j))
    counter[step] += 1

for i in range(1, N):
  print(counter[i])