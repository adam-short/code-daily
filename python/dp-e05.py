from sys import argv
# super bullshit program.
if __name__ == '__main__':
    try:
        if argv[1] == 'adamshort' and argv[2] == 'dddk':
            print("ye.")
        else:
            print("Incorrect.")
    except IndexError:
        print("u needa a username and a password boi.")
