L,R = map(int,input().split())
if L==R:
  print(L%2019 * L%2019)
  exit()
if R-L >= 2019:
  print(0)
  exit()

l = L%2019
r = R%2019
res = 2018
for i in range(l, r+1):
  for j in range(i+1,r+1):
    if (i*j)%2019==  0:
      print(0)
      exit()

    res = min(res, (i*j)%2019)

print(res)

# 一回りしない場合
# l=50,R=2018
# => 0

# 一回りした場合
# l=500,R=100

# ちょうど一周
# l=500,R=500

# 2020~2040 => 1~21
# 2040~20190 => 21~0
# l,r = 21,0 and 21,10
# 2040~4059 => 21~21
# 2040~20190