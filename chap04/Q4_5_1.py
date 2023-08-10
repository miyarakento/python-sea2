a = [sum, min, max]
ai = range(1, 11)
for func in a:
    print("a: {}, Result: {}".format(func.__name__, func(ai)))
