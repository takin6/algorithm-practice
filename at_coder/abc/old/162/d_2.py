from itertools import permutations
N = int(input())
S = input()
# 全ての組み合わせ - (Si=Sj and Si=Sk and SandSk) - (j-i=k-j) 

# res = N**3

# for i in range(N):
#   for j in range(N):
#     for k in range(N):
#       if not i<j<k: 
#         res -= 1
#         continue
      
#       if j-i == k-j:
#         res -= 1
#         continue

#       if S[i]==S[j] or S[i]==S[k] or S[j]==S[k]:
#         res -= 1
#         continue

# print(res)
# r,g,b = [0],[0],[0]
# for i in range(N):
#   if S[i] == "R":
#     r.append(r[-1]+1)
#     g.append(g[-1])
#     b.append(b[-1])
#   elif S[i] == "G":
#     r.append(r[-1])
#     g.append(g[-1]+1)
#     b.append(b[-1])
#   else:
#     r.append(r[-1])
#     g.append(g[-1])
#     b.append(b[-1]+1)

# res = 0
# for i in range(N):
#   for j in range(i+1, N):
#     if S[i] == S[j]: continue
#     diff = j-i

#     if S[i] == "R" and S[j] == "B":
#       pair = (g[-1] - g[j])
#       if j+diff < N and S[j+diff] == "G":
#         pair -= 1
#     elif S[i] == "R" and S[j] == "G":
#       pair = (b[-1] - b[j])
#       if j+diff < N and S[j+diff] == "B":
#         pair -= 1
#     else:
#       pair = (r[-1] - r[j])
#       if j+diff < N and S[j+diff] == "R":
#         pair -= 1

#     print(i,j,S[i],S[j],pair)
#     res += pair

# print(g)
# print(b)
# print(r)
# print(res)

N = int(input())
S = input()
r,g,b = 0,0,0
for i in range(N):
  if S[i] == "R":
    r += 1
  elif S[i] == "G":
    g += 1
  else:
    b += 1

total = r*g*b

for i in range(N):
  for j in range(N):
    if i==j: continue

    k = 2*j - i
    if k > N: continue
    if S[i] == S[k] or S[k] == S[j]: continue
    total -= 1

print(total) 




