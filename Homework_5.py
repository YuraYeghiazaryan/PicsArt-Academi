# coding=utf-8

# Վարժություն 1.13
#       տարբերակ 1

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def fast_pow_iter(m, n, res=1):
    if n == 0:
        return 1
    if is_even(n):
        n = n / 2
        while n > 0:
            res = res * m
            n = n - 1
        return res ** 2
    else:
        n = (n - 1) / 2
        while n > 0:
            res = res * m
            n = n - 1
        return m * (res ** 2)



print(fast_pow_iter(3, 4, 1))
print(fast_pow_iter(3, 7, 1))


# Վարժություն 1.13
#        տարբերակ 2

def fast_pow_iter1(m, n, res=1):
    tmp = 2
    if n == 0:
        return 1
    if not is_even(n):
        n = n - 1
        tmp = 1
    n = n / 2
    while n > 0:
        res = res * m
        n = n - 1
    if tmp == 1:
        return m * (res ** 2)
    return res ** 2


print(fast_pow_iter1(3, 4, 1))
print(fast_pow_iter1(3, 7, 1))
print(" ")

# Վարժություն 1.14

def double(a):
    return a + a


def halve(b):
    if b % 2 == 0:
        return b / 2


def mul(a, b):
    if b == 0:
        return 0
    else:
        return a + mul(a, b - 1)


print(mul(2, 100))


def fast_mul(a, b):
    if b == 0:
        return 0
    if halve(b):
        return double((a + fast_mul(a, b/2 - 1)))
    return a + fast_mul(a, b - 1)


print(fast_mul(2, 100))

