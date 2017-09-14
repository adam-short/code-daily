def num2word(n):
    if n == 0:
        return "zero"
    elif n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    elif n == 4:
        return "four"
    elif n == 5:
        return "five"
    elif n == 6:
        return "six"
    elif n == 7:
        return "seven"
    elif n == 8:
        return "eight"
    elif n == 9:
        return "nine"
    elif n == 10:
        return "ten"
    elif n == 20:
        return "twenty"
    elif n == 30:
        return "thirty"
    elif n == 40:
        return "forty"
    elif n == 50:
        return "fifty"
    elif n == 60:
        return "sixty"
    elif n == 70:
        return "seventy"
    elif n == 80:
        return "eighty"
    elif n == 90:
        return "ninety"
    else:
        ones = n % 10
        tens = n % 100 / 10 * 10
        hundreds = n % 1000 / 100
        thousands = n % 1000000 / 1000
        millions = n % 1000000000 / 1000000

        result = ""
        if millions > 0:
            result += num2word(millions) + " million "

        if thousands > 0:
            result += num2word(thousands) + " thousand "

        if hundreds > 0:
            result += num2word(hundreds) + " hundred "

        if tens > 0:
            result += num2word(tens) + " "

        if ones > 0:
            result += num2word(ones)

        return result

strp = raw_input("> ")
print(num2word(int(strp)))
