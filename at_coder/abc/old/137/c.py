from collections import defaultdict
N = int(input())
counter = defaultdict(int)

for _ in range(N):
  s = input()
  alpha = [0] * 26
  a = ord("a")
  for c in s:
    alpha[ord(c)-a] += 1 
  counter[tuple(alpha)] += 1

res = 0
for k,v in counter.items():
  res +=v*(v-1)//2

print(res)
print(counter)