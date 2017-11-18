from sys import argv

if __name__ == '__main__':
    try:
        nums = sorted(argv[1:4], reverse=True)
        print(int(nums[0])**2 + int(nums[1])**2)
    except IndexError:
        print("You need to give me 3 numbers.")
    except TypeError:
        print("The three args must be numbers.")
