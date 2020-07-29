class Combination:
    """
    O(n)の前計算を1回行うことで，O(1)でnCr mod mを求められる
    n_max = 10**6のとき前処理は約950ms (PyPyなら約340ms, 10**7で約1800ms)
    使用例：
    comb = Combination(1000000)
    print(comb(5, 3))  # 10
    """
    def __init__(self, n_max, mod=10**9+7):
        self.mod = mod
        self.modinv = self.make_modinv_list(n_max)
        self.fac, self.facinv = self.make_factorial_list(n_max)

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

    def make_factorial_list(self, n):
        # 階乗のリストと階乗のmod逆元のリストを返す O(n)
        # self.make_modinv_list()が先に実行されている必要がある
        fac = [1]
        facinv = [1]
        for i in range(1, n+1):
            fac.append(fac[i-1] * i % self.mod)
            facinv.append(facinv[i-1] * self.modinv[i] % self.mod)
        return fac, facinv

    def make_modinv_list(self, n):
        # 0からnまでのmod逆元のリストを返す O(n)
        modinv = [0] * (n+1)
        modinv[1] = 1
        for i in range(2, n+1):
            modinv[i] = self.mod - self.mod//i * modinv[self.mod%i] % self.mod
        return modinv

# N,A,B = map(int,input().split())
# combination = Combination(N+1)

# print(combination[N,])

def nCr(n,r):
    dividend, divisor = 1, 1
    for i in range(r):
        dividend *= n-i
        divisor *= i+1
        dividend %= MOD
        divisor %= MOD
    return (dividend * pow(divisor, MOD-2, MOD)) % MOD

N,A,B = map(int,input().split())
MOD = 10**9+7
print((pow(2, N, MOD) - 1 - nCr(N,A) - nCr(N,B)) % MOD)


# N, A, B = list(map(int, input().split()))
# MAX_INT = 10**9 + 7

# def choose(n, k):
#   x, y = 1, 1
#   for i in range(k):
#     x = x * (n-i) % MAX_INT
#     y = y * (k-i) % MAX_INT

#   return ( x * pow(y, MAX_INT-2, MAX_INT) ) % MAX_INT

# print( (pow(2, N, MAX_INT) - 1 - choose(N, A) - choose(N, B)) % MAX_INT)
