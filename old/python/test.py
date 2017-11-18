def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
def all_lengths(iterable):
    return range(1, len(iterable)+1)
def solution(iterable):
    lengths = all_lengths(iterable)
    results = []
    for l in lengths: 
        results.append(combinations(iterable, l))
    
    return results
print(solution([1,2,3]))
