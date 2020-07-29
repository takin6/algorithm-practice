S = list(input())
N = len(S)
res = [0] * N

def calc(pivot_r, pivot_l, r_count, l_count):
  # print(pivot_r, pivot_l, r_count, l_count)
  common = (r_count+l_count)//2
  res[pivot_r], res[pivot_l] = 1+common, 1+common
  if (r_count+l_count)%2 == 1:
    if r_count > l_count:
      res[pivot_r] += 1
    else:
      res[pivot_l] += 1

  if max(r_count,l_count) % 2 == 1:
    res[pivot_r], res[pivot_l] = res[pivot_l], res[pivot_r]


cur = "R"
r_count = 0
l_count = 0
pivot_r = 0
pivot_l = 0
for i in range(N):
  if S[i] == cur:
    if cur=="R": r_count += 1
    if cur=="L": l_count += 1
  else:
    if cur=="R": 
      cur = "L"
      pivot_r = i-1
      pivot_l = i
    elif cur=="L":
      calc(pivot_r,pivot_l,r_count-1,l_count)
      cur ="R"
      r_count,l_count = 1,0
      pivot_r,pivot_l = 0,0
calc(pivot_r,pivot_l,r_count-1,l_count)

print(" ".join(map(str, res)))