a = {x for x in range(21)}
print(a)
b = {x for x in range(21) if x % 2 == 0}
print(b)
c = a - b
print(c)
