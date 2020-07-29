# N個のブロック、M色、K組
# def power(x, a):
#   if a == 0:
#     return 1
#   elif a == 1:
#     return x
#   elif a % 2 == 0:
#     return power(x, a//2) **2 % MOD
#   else:
#     return power(x, a//2) **2 * x % MOD

# def modinv(x):
#   return power(x, MOD-2)

# def nCr(n,r):
#   mul, div = 1, 1
#   for i in range(r):
#     mul *= (n-i)
#     div *= (i+1)
#     mul %= MOD
#     div %= MOD
#   # return mul * pow(div,MOD-2,MOD) % MOD
#   return mul * modinv(div) % MOD


N,M,K = map(int,input().split())
MOD = 998244353

class Combination:
  def __init__(self, n_max, mod=998244353):
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

comb = Combination(2*10**5)

res = 0
# memp = pow(M-1, N-x-1, MOD)
for x in range(K+1):
  res += (M * pow(M-1, N-x-1, MOD)%MOD * comb(N-1, x)%MOD)%MOD
  res %= MOD

print(res % MOD)
# print((M*pow(M-1, N-K-1, MOD) * nCr(N-1, K)) % MOD)


# え、どういうこと？
# https://atcoder.jp/contests/abc167/submissions/13641583

# Combinationのライブラリ
# https://atcoder.jp/contests/abc167/submissions/13398359
