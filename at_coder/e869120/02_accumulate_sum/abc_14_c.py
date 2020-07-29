N = int(input())
colors = [0] * 1000002

for i in range(N):
  a,b = map(int,input().split())
  colors[a] += 1
  colors[b+1] += -1

for i in range(1000000):
  colors[i+1] += colors[i]

print(max(colors))
# print(colors[:10])
# print(colors.count(N)) 