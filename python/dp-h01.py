
def guess(high, low):
    return round(low + (high - low) / 2.0)

if __name__ == '__main__':
    high, low = 100, 0
    while True:
        current = guess(high, low)
        print(current)

        inp = raw_input("H/L/D > ")
        if inp == "H":
            low = current
        elif inp == "L":
            high = current
        elif inp == "D":
            print("Yay!")
            break
