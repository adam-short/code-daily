from sys import argv

def simple_interest(principal, rate, periods):
    return principal * (rate / 100) * periods

def compound_interest(principal, rate, periods):
    return principal * (1 + (rate / 100))**periods

if __name__ == '__main__':
    if len(argv) != 5:
        print("Usage: TYPE PRINCIPAL RATE PERIODS")

    if argv[1] == 'simple':
        print(simple_interest(*argv[2:]))
    elif argv[1] == 'compound':
        print(compound_interest(*argv[2:]))
    else:
        print('')
