def fib(n):
    a, b = 0, 1
    while a < n:
        c = a + b
        print(c)
        a = b
        b = c


fib(1000)
