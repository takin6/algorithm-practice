A = [1, 5, 7]
n = 3
target = 8
i = 0

def solve(i, t, m=None):
  print(i, t, m)
  if t == 0:
    return True
  if i >= n:
    return False

  res = solve(i+1, t, "do nothing") or solve(i+1, t-A[i], "calc") 

  print(res)
  return res


print(solve(i, target))