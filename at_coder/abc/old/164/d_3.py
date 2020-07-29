from collections import Counter
S = input()
S = S[::-1]
N = len(S)
counter = Counter()
counter[0] = 1
prev = 0
MOD = 2019
for i in range(N):
  c = (int(S[i]) * pow(10, i, MOD) )%MOD
  prev = (prev+c)%MOD
  counter[prev] += 1

ans = 0
for k,v in counter.items():
  ans += (v * (v-1))//2


print(ans)