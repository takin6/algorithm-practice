A,B = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# dp[i][j]=Aからi個、Bからj個取った状態での先攻のスコア
dp = [ [0]*(B+1) for _ in range(A+1) ]

for i in range(A, -1, -1):
    for j in range(B, -1, -1):
        if i == A and j == B: continue
        # print(i,j)
        # 先攻
        if (i+j) % 2 == 0:
            if i == A:
                dp[i][j] = b[j]+dp[i][j+1]
            elif j == B:
                dp[i][j] = a[i]+dp[i+1][j]
            else:
                dp[i][j] = max(dp[i][j], a[i]+dp[i+1][j], b[j]+dp[i][j+1])
        # 後攻
        else:
            if i == A:
                dp[i][j] = dp[i][j+1]
            elif j == B:
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j+1])

print(dp[0][0])
