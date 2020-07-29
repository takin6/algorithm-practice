def factorial(n):
  if n <= 1:
    return 1

  return n * factorial(n-2)

i = int(input())
r = list(str(factorial(i)))

ans = 0
for i in range(len(r)-1, 0):
  if r[i] == 0:
    ans += 1
  else:
    break

print(ans)