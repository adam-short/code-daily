def solution(number):
    return sum(x for x in range(number) if x % 5 == 0 or x % 3 == 0)


def solution_simple(number):
    total = 0
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    return total


print("{}, {}".format(solution(10),solution_simple(10)))
print("{}, {}".format(solution(200), solution_simple(200)))
