# cats: N (even)
# cats: 1~N
# - 首に赤いスカーフを巻いている、好きな整数が一つ（>0）
# - xor
#   - 

N = int(input())
A = list(map(int,input().split()))
cumsum = [0]
for a in A:
  cumsum.append(cumsum[-1]^a)

res = []
for i in range(N):
  res.append(cumsum[-1]^A[i])

print(" ".join(map(str, res)))
print(res)
