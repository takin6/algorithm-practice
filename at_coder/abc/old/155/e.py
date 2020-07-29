# n = list(map(int, list(input())))
# n.reverse()
# n.append(0)
# ans = 0
 
# for i in range(len(n)):
#     # d <= 4 -> and += d
#     # d == 5 -> next d <= 4 ans += d else ans += d next digit += 1
#     # d >= 6 -> ans += 10 - d next digit += 1
#     if n[i] <= 4:
#         ans += n[i]
#     elif n[i] == 5:
#         if n[i + 1] <= 4:
#             ans += n[i] 
#         else:
#             ans += n[i]
#             n[i + 1] += 1
#     else:
#         ans += 10 - n[i]
#         n[i + 1] += 1
#         import pdb; pdb.set_trace()
# print(ans)

# def read():
#     N = input().strip()
#     return N,
 
 
# def solve(N, INF=1000000):
#     L = len(N)
#     N = list(reversed("0" + N))
#     # そのまま足したとき
#     dp0 = [0 for i in range(L + 1)]
#     # -1して足したとき
#     dp1 = [0 for i in range(L + 1)]
#     dp1[0] = INF
#     for i in range(L):
#         x = int(N[i])
#         # 前の桁が繰り下がっていない vs. 繰り上がったとき
#         dp0[i + 1] = min(dp0[i] + x, dp1[i] + x)
#         # 前の桁が繰り下がっていない場合に繰り上げた vs.
#         # 前の桁が繰り上がって、かつ次の桁も繰り上げる
#         dp1[i + 1] = min(dp0[i] + 1 + (10 - x), dp1[i] + 1 + (10 - x) - 2)
#         print(i)
#         print(dp0, dp1)

#     return min(dp0[-1], dp1[-1])
 
 
# if __name__ == '__main__':
#     inputs = read()
#     print("{}".format(solve(*inputs)))


# s = "91"
# s = "".join([ i for i in reversed(s)]) + "0"

# import pdb; pdb.set_trace()
# n = len(s)
# INF = 10 ** 23
# dp = [ [INF] * 2 for _ in range(n)]
# dp[0][0] = 0

# for i in range(n-1):
#     for j in range(0, 2):
#         x = int(s[i])
#         x += j
#         for a in range(10):
#             ni, nj = i+1, j
#             b = a - x

#             if b < 0:
#                 nj = 1
#                 b += 10

#             print(ni, nj, a)
#             dp[ni][nj] = min(dp[ni][nj], dp[i][j]+a+b)
#             print(dp)

# print(dp[n-1][0])



# s = "91"
# s = "".join([ i for i in reversed(s)]) + "0"

# n = len(s)
# INF = 10 ** 23
# dp = [ [INF] * 2 for _ in range(n)]
# dp[0][0] = 0

# for i in range(n-1):
#     dp[0][i+1]=min(dp[0][i]+int(s[i]),dp[1][i]+(int(s[i])+1));
#     dp[1][i+1]=min(dp[0][i]+10-(int(s[i])),dp[1][i]+10-(int(s[i])+1));

# print(dp[n-1][0])


# s = "314159265358979323846264338327950288419716939937551058209749445923078164062862089986280348253421170"
# s = "91"
# s = "3141592"
# s = input()
s = "".join([ i for i in reversed(s)]) + "0"

INF = 10 ** 32
n = len(s)
dp = [ [INF]*2 for _ in range(n)]

dp[0][0] = 0

for i in range(n-1):
    for j in range(0, 2):
        x = int(s[i])

        # dp[i+1][0] = min( dp[i][0]+x, dp[i][1]+x )
        # # i番目で繰り上がっていたら、(10-1)-x
        # dp[i+1][1] = min( dp[i][0]+1+(10-x), dp[i][1]+(9-x) )

        # if x + j < 10: dp[i+1][0] = min( dp[i+1][0], dp[i][j]+x )
        # if x + j < 10: dp[i+1][0] = min( dp[i+1][0], dp[i][j]+x )

        # (0, 0), (0)
        # Aiをxにして、Biを0にする
        if x + j < 10: dp[i+1][0] = min( dp[i+1][0], dp[i][j]+x )
        # Aiを0にして、Biを10-x
        if x + j > 0: dp[i+1][1] = min( dp[i+1][1], dp[i][j]+(10-x) )

print(min(dp[n-1][0], dp[n-1][1]))
