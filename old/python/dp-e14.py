from itertools import chain

def split_in_chunks(ls, size):
    newls = []
    for i in xrange(0, len(ls), size):
        newls.append(ls[i:i+size])
    return newls

def reverse_chunks(chunks):
    return [x[::-1] for x in chunks]

def flatten_chunks(chunks):
    return list(chain(*chunks))

chunks = split_in_chunks(raw_input("list > ").split(), int(raw_input("chunk > ")))
reversedchunks = reverse_chunks(chunks)
flattenedchunks = flatten_chunks(reversedchunks)

print(' '.join(flattenedchunks))
