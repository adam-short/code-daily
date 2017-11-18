from sys import argv

if __name__ == '__main__':
    try:
        if argv[2] == '-i':
            ints = map(int, argv[1])
            print(sorted(ints))
        elif argv[2] == '-s':
            print(sorted(argv[1]))
        else:
            print('ERROR: Use either -i or -s flag.')
    except IndexError as e:
        print("ERROR: Missing an argument.")
    except ValueError as e:
        print("ERROR: Tried to use letters as numbers.")
