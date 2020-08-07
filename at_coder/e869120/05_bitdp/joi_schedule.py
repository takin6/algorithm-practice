N = int(input())
q = [0]
MOD = 10007
for i in input():
  if i=="J":
    q.append(1<<0)
  elif i=="O":
    q.append(1<<1)
  else:
    q.append(1<<2)

# dp[S][i] = i日目に部分集合Sが出席したときの、0~i日までのスケジュールの決め方の総和
dp = [ [0]*(N+1) for _ in range(1<<3) ]
# 0日目にj君1人だけ
dp[1][0] = 1

for i in range(N):
  for now in range(1<<3):
    for next in range(1<<3):
      if now&next:
        if next&q[i+1]:
          dp[next][i+1] += dp[now][i]
          dp[next][i+1] %= MOD

ans = 0
for i in range(1<<3):
  ans += dp[i][N]
  ans %= MOD
print(ans)



# https://algo-logic.info/bit-dp/#toc_id_4