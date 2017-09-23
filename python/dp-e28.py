
def brute_force(ls):
    return next(x for x in ls if ls.count(x) > 1)
