
count_bottles = "{} bottles of beer on the wall, {} bottles of beer."
remove_bottle = "Take one down and pass it around, {} bottles of beer on the wall."
no_more = "No more bottles of beer on the wall, no more bottles of beer."
finisher = "Go to the store and buy some more, 99 bottles of beer on the wall."

if __name__ == '__main__':
    for b in range(1, 100)[::-1]:
        print(count_bottles.format(b, b))
        print(remove_bottle.format(b-1 if b-1>0 else 'no more'))

    print(no_more)
    print(finisher)
