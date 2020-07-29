N,M = map(int,input().split())

wa_count = { i+1: 0 for i in range(N) }
ac_count = { i+1: False for i in range(N) }
wa,ac = 0,0

for _ in range(M):
  p,s = map(str,input().split())
  p = int(p)
  if s == "AC" and not ac_count[p]:
    ac += 1
    wa += wa_count[p]
    ac_count[p] = True
  else:
    wa_count[p] += 1

print(ac, wa)