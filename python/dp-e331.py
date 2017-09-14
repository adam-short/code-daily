
base, power = map(int, raw_input("Enter BASE POWER > ").split(' '))
pow_digits = map(int, list(str(base ** power)))

print(sum(pow_digits))
print(pow_digits)
