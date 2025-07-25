l1 = [23,65,22,76,34,98,43]
it = iter(l1)


while True:
    try :
        print(next(it))
    except StopIteration:
        break