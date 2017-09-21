import sys

def standard_triangle(height):
    return '\n'.join(["@"*(2*x-1) for x in range(0, height+1)])

def reverse_triangle(height):
    return '\n'.join(["@"*(2*x-1) for x in range(0, height+1)[::-1]])

if __name__ == '__main__':
    try:
        height = int(sys.argv[1])
        print(standard_triangle(height))
        print(reverse_triangle(height))
    except IndexError as e:
        print("Requires height.")
    except ValueError as e:
            print("")
