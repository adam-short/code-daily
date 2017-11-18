def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 + -n2

def mul(n1, n2):
    res = 0
    for _ in range(abs(n2)):
        if n2 > 0:
            res += n1
        elif n2 < 0:
            res = sub(res, n1)
        else:
            return 0
    return res

def div(n1, n2):
    count = 0
    res = abs(n1)
    while res != 0:
        if sub(res, abs(n2)) < 0:
            return "Non-integeral answer."
        res = sub(res, abs(n2))
        count += 1

    return count if n2 > 0 and n1 > 0 else -count

def exponent(n1, n2):
    if n2 == 0:
        return 1
    elif n2 < 0:
        return "Non-integeral answer."
    res = n1
    for _ in range(n2-1):
        res = mul(res, n1)
    return res

def components(expression):
    exp_components = expression.split(' ')
    return int(exp_components[0]), exp_components[1], int((exp_components[2]))

def compute(num1, operator, num2):
    if num1 == 0 and num2 == 0 and operator == "/":
        return "Not-defined."

    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return sub(num1, num2)
    elif operator == "*":
        return mul(num1, num2)
    elif operator == "/":
        return div(num1, num2)
    elif operator == "^":
        return exponent(num1, num2)
    else:
        return "Operator unknown."

if __name__ == '__main__':
    while True:
        expression = raw_input(">  ")
        num1, operator, num2 = components(expression)
        print(compute(num1, operator, num2))
