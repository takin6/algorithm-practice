def attack(h):
  if h == 1:
    return 1
  
  return 2 * attack(h // 2) + 1

H = int(input())
print(attack(H))