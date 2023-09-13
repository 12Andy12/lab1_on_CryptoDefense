import math
import Fast_pow


def solve(g: int, a: int, p: int) -> int or None:
    k = int(math.sqrt(p)) + 1
    gk = pow(g, k, p)
    y = gk
    h = {}  # словарь, ключи - элементы группы, значения - степени порождающего элемента
    for i in range(1, k + 1):
        h[y] = i
        y = y * gk % p

    for j in range(0, k):
        r = a * pow(g, j) % p
        i = h.get(r, -1)
        if i != -1:
            return i * k - j


def start():
    print('g^(x) mod p = a')
    g = 2
    a = 16190
    p = 30803
    print(f"where:\ng = {g}\np = {p}\na = {a}\nCalculeting\n . . .")
    x = solve(g, a, p)
    print(f"Completed\nx = {x}\n\nCheck:")
    print(f"({g})^(x) % {p} = {a}")
    print(f"({g})^({x}) % {p} = {Fast_pow.mega_pow(g, x, p)}")
