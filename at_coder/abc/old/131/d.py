N = int(input())
W = []
for _ in range(N):
  a,b = map(int,input().split())
  W.append((a,b))
W.sort(key=lambda x: x[1])

cur = 0
for a,b in W:
  if cur+a > b:
    print("No")
    exit()
  cur += a 

print("Yes")