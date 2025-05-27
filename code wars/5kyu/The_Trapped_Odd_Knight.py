"""
We have an endless chessboard, and on each cell there is a number written in a spiral.

16ㅤㅤ15ㅤㅤ14ㅤㅤ13ㅤㅤ12

17ㅤㅤ4 ㅤㅤ3 ㅤㅤ2 ㅤㅤ11

18ㅤㅤ5 ㅤㅤ0 ㅤㅤ1 ㅤㅤ10

19ㅤㅤ6 ㅤㅤ7 ㅤㅤ8 ㅤㅤ9ㅤㅤ...

20ㅤㅤ21ㅤㅤ22ㅤㅤ23ㅤㅤ24ㅤㅤ25

And we have a knight. A normal chess knight moves +1 to one axis and +2 to the other. But this knight moves +n to one axis and +m to the other.

And this knight has two more rules: He cannot move to the same square twice, and he only moves to the smallest available square. For example, an ordinary knight (n=1, m=2) starts his journey like this:

0 -> 9 -> 2 -> 5 -> 8 -> ...

But someday he will reach a cell from which he will not be able to get out without violating the rule, it is this last cell that the function must return. For this case it 2083

Performance requirements:

Values of m up to 300_000_000 will be tested in fixed tests. Multiple random tests with m up to 20_000. You will always have 0 < n < m.
"""


def coord_to_val(x, y):
    a = max(abs(x), abs(y))
    if a == 0:
        return 0

    base = (2 * a - 1) ** 2

    if y == a:
        return base + (a + x - 1)
    elif x == a:
        return base + (3 * a - y - 1)
    elif y == -a:
        return base + (5 * a - x - 1)
    else:  # x == -a
        return base + (7 * a + y - 1)

def trapped_cell(n: int, m: int) -> int:
    moves = {(n, m), (n, -m), (m, n), (m, -n), (-n, m), (-n, -m), (-m, n), (-m, -n)}
    seen = {0}
    x = y = val = 0

    while True:
        candidates = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            nv = coord_to_val(nx, ny)
            if nv not in seen:
                candidates.append((nv, nx, ny))

        if not candidates:
            return val

        val, x, y = min(candidates)
        seen.add(val)



print(f"output: {trapped_cell(1, 2)} | expected: {2083}")
print(f"output: {trapped_cell(2, 3)} | expected: {4697}")
print(f"output: {trapped_cell(3, 4)} | expected: {1163}")
print(f"output: {trapped_cell(4, 5)} | expected: {6499}")
print(f"output: {trapped_cell(5, 6)} | expected: {1201}")
