def LI():
  return list(map(int,input().split()))

def I():
  return int(input())

S = input()
T = input()

res = 0
for i,s in enumerate(S):
  if T[i] != s:
    res += 1
print(res)