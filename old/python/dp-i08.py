import sys

def num2word(n):
    n2w = {
        "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
        "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine",
        "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen",
        "14": "fourteen", "15": "fifteen", "16": "sixteen", "17": "seventeen",
        "18": "eighteen", "19": "nineteen", "20": "twenty", "30": "thirty",
        "40": "forty", "50": "fifty", "60": "sixty", "70": "seventy",
        "80": "eighty", "90": "ninety"
    }
    if str(n) in n2w:
        print(str(n))
        return n2w[str(n)]
    else:
        ones, tens, hundreds = n % 10, n % 100, n % 1000 / 100
        thousands, millions = n % 1000000 / 1000,  n % 1000000000 / 1000000
        result = ""
        if millions > 0:
            result += num2word(millions) + " million "

        if thousands > 0:
            result += num2word(thousands) + " thousand "

        if hundreds > 0:
            result += num2word(hundreds) + " hundred "

        if 0 < tens < 20:
            result += n2w[str(tens)]
        else:
            result += num2word(tens / 10 * 10) + " "

        if ones > 0 and tens >= 20:
            result += num2word(ones)

        return result

word = sys.argv[1]
print(num2word(int(word)))
