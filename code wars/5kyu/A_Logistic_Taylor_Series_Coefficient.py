"""
https://www.codewars.com/kata/674c0718cec27cf1f2606070/train/python
"""

MOD = 10**9 + 7
INV2 = (MOD + 1) // 2

def compute_coefficient(n: int) -> int:
    if n == 0:
        return 1
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    invfact = [1] * (n + 1)
    invfact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD

    def C(nn, kk):
        return fact[nn] * invfact[kk] % MOD * invfact[nn - kk] % MOD

    a = [0] * (n + 1)
    a[0] = 1
    if n >= 1:
        a[1] = 1

    for m in range(1, n):
        s = 0
        for k in range(m + 1):
            s = (s + C(m, k) * a[k] % MOD * a[m - k]) % MOD
        a[m + 1] = s * INV2 % MOD

    return a[n]