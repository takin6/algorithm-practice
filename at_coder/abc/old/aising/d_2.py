N = int(input())
X = input()
val = int(X,2)

cnt1 = X.count("1")
p_cnt = cnt1+1
m_cnt = cnt1-1
p_amari = val%(cnt1+1)
if cnt1-1 != 0:
  m_amari = val%(cnt1-1)
else:
  m_amari = 0

def f(x):
  if x==0: return 0
  return 1 + f(x%bin(x).count("1"))

for i in range(N):
  ans = 0
  if X[i] == "0":
    amari = p_amari + pow(2,N-i-1,p_cnt)
    amari %= p_cnt
    ans += 1
  else:
    if cnt1-1==0:
      print(0)
      continue
    amari = m_amari - pow(2,N-i-1,m_cnt)
    amari %= m_cnt
    ans += 1

  ans += f(amari)
  print(ans)

# https://atcoder.jp/contests/aising2020/submissions/15160205