
# Failed Attempt
def xbonacci(sig, n):
    sum_distance = len(sig)
    seq = sig
    for i in range(0, n-sum_distance+1):
        print(sig, i, sum_distance)
        print("{} sums to {}".format(sig[i:i+sum_distance], sum(sig[i:i+sum_distance])))
        seq.append(sum(sig[i:i+sum_distance]))
    return seq[:-1]


# Best Practise
def xbonacci_best(signature,n):
    output, x = signature[:n], len(signature)
    while len(output) < n:
        output.append(sum(output[-x:]))
    return output