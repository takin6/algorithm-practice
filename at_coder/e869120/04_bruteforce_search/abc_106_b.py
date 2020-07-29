N = int(input())

res = 0
for i in range(1,N+1):
  if i%2==0: continue
  cnt = 0
  num = i
  for j in range(1, int(i**0.5)+1):
    if num%j==0:
      cnt += 1
      if j != num//j:
        cnt += 1

  if cnt == 8: 
    res += 1

print(res)