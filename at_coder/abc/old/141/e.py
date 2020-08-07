# l1 + len <= l2
# S[l1+i] = S[l2+i] (i=0,1,...,len-1)

def z_algorithm(s):
  n = len(s)
  z = [0] * n
  z[0] = n

  i,j = 1,0
  while i < n:
    while i+j<n and s[j]==s[i+j]:
      j += 1
    z[i] = j

    if j==0:
      i += 1
      continue

    k = 1
    while k+z[k]<j:
      z[i+k] = z[k]
      k+= 1

    i+=k
    j-=k

  return z

n = int(input())
s = input()
ans = 0
for i in range(n):
  z = z_algorithm(s[i:])
  for j in range(n-i):
    if z[j]<=j:
      ans = max(ans, z[j])

print(ans)

# z-algorithm
# https://atcoder.jp/contests/abc141/submissions/14794620

# normal dp
# https://atcoder.jp/contests/abc141/submissions/14684216