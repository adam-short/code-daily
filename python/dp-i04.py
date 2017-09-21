import sys

def operate(symbol, n1, n2):
    if symbol == "*":
        return int(n1) * int(n2)
    elif symbol == "/":
        return int(n1) / int(n2)
    elif symbol == "+":
        return int(n1) + int(n2)
    elif symbol == "-":
        return int(n1) - int(n2)


# 5 * 5 + 3 - 2 -> ["5 * 5", "+ 3", " - 2"]
# doesn't follow order of operations.
def calculate(exp):
    result = operate(exp[1], exp[0], exp[2])
    for i in range(3, len(exp), 2):
        result = operate(exp[i], result, exp[i+1])

    return result


print(calculate(sys.argv[1].split()))
