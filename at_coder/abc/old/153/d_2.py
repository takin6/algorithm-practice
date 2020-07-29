H = int(input())
memo = {}
def attack(h):
  if h in memo: return memo[h]

  if h <= 1:
    memo[h] = 1
    return memo[h]
  else:
    memo[h//2] = attack(h//2)
    return 1 + memo[h//2] + memo[h//2]

print(attack(H))