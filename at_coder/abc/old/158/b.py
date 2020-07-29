N, A, B = list(map(int, input().split()))

res = 0

res += (N // (A+B)) * A

res += min((N % (A+B)), A)

print(res)