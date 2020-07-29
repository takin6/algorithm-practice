from collections import Counter
S = input()[::-1]
cur = 0
mods = Counter()
mods[0] += 1
MOD = 2019
for i,d in enumerate(S):
  cur += int(d) * pow(10, i, MOD)
  mods[cur%MOD] += 1

res = 0
for k,v in mods.items():
  res += (v * (v-1) // 2)

print(res)