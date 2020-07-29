import itertools
# a,b,c = map(int, input().split())

# gcd(0,2) = 2
def gcd(a,b):
    a,b = max(a,b), min(a,b)
    if b == 0: return a
    while a%b != 0:
        a,b = b,a%b
    return b

# coords = set()
# for i in range(a+1):
#     for j in range(b+1):
#         coords.add((i,j))

# res = 0
# for p1,p2 in itertools.combinations(coords,2):
#     x1,y1 = p1
#     x2,y2 = p2
#     if gcd(abs(x1-x2),abs(y1-y2))+1 == c:
#         res += 1 

# print(res)

n, m, k = map(int, input().split())
ans = 0
for i in range(n + 1):
  for j in range((1 if i == 0 else 0), m + 1):
    if gcd(i, j) == k - 1:
      if 0 < i and 0 < j:
        ans += (n - i + 1) * (m - j + 1) * 2
      else:
        ans += (n - i + 1) * (m - j + 1)
print(ans)