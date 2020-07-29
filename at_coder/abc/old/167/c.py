N,M,X = map(int,input().split())
books = []

for _ in range(N):
  info = list(map(int,input().split()))
  books.append(info)

res = float('inf')
for i in range(1<<N):
  scores = [0] * M
  cost = 0
  for j in range(N):
    if (i>>j)&1:
      for k,p in enumerate(books[j][1:]):
        scores[k] += p
      cost += books[j][0]

  if all([ score >= X for score in scores]):
    res = min(res, cost)

print(res) if res < float('inf') else print('-1')