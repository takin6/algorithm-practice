N = int(input())
P = list(map(int,input().split()))

cur_min = 10**15
res = 0
for i in P:
  if i < cur_min:
    cur_min = i
    res += 1

print(res)    
