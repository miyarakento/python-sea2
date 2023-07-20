def ja(*args):
    result = []
    for n in args:
        result.append(n * n)
    return result


number = [1, 2, 3, 4]
ja(*number)


jia = list(range(100))
print(ja(*jia))
