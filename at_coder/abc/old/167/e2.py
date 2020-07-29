class Combination:
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

N,M,K = map(int,input().split())
ans = 0
MOD = 998244353
comb = Combination(2*(10**5)+1, MOD)
for i in range(K+1):
  res = (M * pow(M-1, N-i-1, MOD)%MOD * comb(N-1, i)%MOD)%MOD
  ans = (ans + res)%MOD

print(ans)

# res += (M * pow(M-1, N-x-1, MOD)%MOD * comb(N-1, x)%MOD)%MOD