from random import randint


def to_bin(x):
    s = ""
    while x != 0:
        s = s + str(x % 2)
        x //= 2

    return s


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def ferma(x):
    if x == 2:
        return True
    for i in range(0, 100):
        a = randint(2, x - 2)
        if gcd(a, x) != 1:
            return False
        if mega_pow(a, x - 1, x) != 1:
            return False
    return True


def mega_pow(x, n, y):
    bin_n = to_bin(n)
    result = 1
    list = []
    for i in range(0, len(bin_n)):
        if bin_n[i] == '1':
            result *= x
        x = (x * x) % y

    return result % y


def test(x, n, mod):
    print("mega_pow({0}, {1}, {2}) = {3}".format(x, n, mod, mega_pow(x, n, mod)))
    print("{0} ** {1} % {2} = {3}".format(x, n, mod, pow(x, n, mod)))


def test1():
    mod = randint(0, 10 ** 9)
    while not ferma(mod):
        mod = randint(0, 10 ** 9)

    x = randint(0, mod - 1)

    n = randint(0, 10 ** 9)
    print("mega_pow({0}, {1}, {2}) = {3}".format(x, n, mod, mega_pow(x, n, mod)))
    print("{0} ** {1} % {2} = {3}".format(x, n, mod, pow(x, n, mod)))
