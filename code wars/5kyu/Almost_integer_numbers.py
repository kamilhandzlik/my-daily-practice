"""
Uncopyable.
In short get smallest integer bigger than result of this equation
(a * sqrt(b))^k
"
For given natural numbers  compute the smallest integer, which is bigger or equal than
(a * sqrt(b))^k
"
Because the results may be large, return them modulo  MOD
1 < A < 10^9
(A-1)^2 < B < A^2
1 < A < 10^9
1 < k < 10^9
"""

# Solution 1 works but is overly complicated
MOD = 10 ** 9 + 7


def f(a, b, k):
    MOD = 10**9 + 7
    if a < 1 or a > 10**9 or (a-1)**2 > b or b > a**2 or k < 1 or k > 10**9:
        return MOD

    def mat_mult(A, B):
        return [
            [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
            [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
        ]

    def mat_pow(mat, power):
        result = [[1, 0], [0, 1]]
        while power:
            if power % 2:
                result = mat_mult(result, mat)
            mat = mat_mult(mat, mat)
            power //= 2
        return result

    c = 2 * a % MOD
    d = (a * a - b) % MOD
    base_matrix = [
        [c, (MOD - d) % MOD],
        [1, 0]
    ]

    if k == 0:
        return 2
    elif k == 1:
        return (2 * a) % MOD

    mat_k = mat_pow(base_matrix, k - 1)
    T_k = (mat_k[0][0] * (2 * a) + mat_k[0][1] * 2) % MOD
    return T_k



print(f(1015, 1029777, 3))
print(f(8, 50, 2))
print(f(2, 3, 166860621))
