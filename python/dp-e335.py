import sys


def distance_between(arr, n1, n2):
    return arr.index(n2) - arr.index(n1)


def distance_rating(arr):
    pool = sorted(arr)
    distance = 0
    for i in xrange(len(pool)-1):
        print(pool[i], pool[i+1])
        distance += abs(distance_between(arr, pool[i], pool[i+1]))

    return distance


def consecutives(arr):
    return [x[1] for x in enumerate(arr) if x[0] != 0 and arr[x[0]-1] == x[1] - 1]


def consec_distance_rating(arr):
    pool = consecutives(sorted(arr))
    distance = 0
    for i in xrange(0,len(pool)-1):
        print(pool[i], pool[i+1])
        distance += abs(distance_between(arr, pool[i], pool[i+1]))

    return distance


if __name__ == "__main__":
    try:
        target = map(int, sys.argv[1].split(" "))
    except IndexError as e:
        print("Must provide a string of space seperated, unique integers.")
    
    print("pool:            {}".format(target))
    print("ordered_pool:    {}".format(sorted(target)))
    print("consecutives:    {}".format(consecutives(sorted(target))))
    print("consec rating:   {}".format(consec_distance_rating(target)))
