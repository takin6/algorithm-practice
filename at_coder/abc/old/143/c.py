# slime: N
# colors: S: str
N = int(input())
S = input()

ans = 0
prev = ""
for s in S:
  if s != prev:
    prev = s
    ans += 1
  else:
    continue

print(ans)