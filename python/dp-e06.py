from sys import argv
from decimal import Decimal, getcontext

getcontext().prec = 90


def seedk(k):
    return 1 / Decimal(16) ** k

def k8_1(k):
    return Decimal(4) / (8 * k + 1)

def k8_4(k):
    return Decimal(2) / (8 * k + 4)

def k8_5(k):
    return Decimal(1) / (8 * k + 5)

def k8_6(k):
    return Decimal(1) / (8 * k + 6)

def BBP_FORMULA(n):
    return seedk(n) * (k8_1(n) - k8_4(n) - k8_5(n) - k8_6(n))

def guess_pi(n):
    return sum(BBP_FORMULA(k) for k in range(n))

if __name__ == '__main__':
    try:
        result = guess_pi(int(argv[1]))
        print(result)
    except IndexError:
        print("Give me # of sides.")
