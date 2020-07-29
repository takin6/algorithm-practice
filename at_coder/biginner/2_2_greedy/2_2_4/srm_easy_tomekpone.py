import sys

freq = sorted(list(map(int, input().split())), reverse=True)
ints = sorted(list(map(int, input().split())))

strokes = []
for i in ints:
  for j in range(1, i+1):
    strokes.append(j)

strokes = sorted(strokes)

if len(strokes) < len(freq):
  print(-1)
  sys.exit(0)

res = 0
while freq:
  key = freq.pop(0)
  s = strokes.pop(0)
  res += key * s

print(res)
