def f(x):
    c = 0
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            c += 1
            if x % (x // i) == 0:
                c += 1
    if c == 0:
        return True
    return False

cn = 0
for x in range(182635, 453734):
    c = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            c.add(i)
            c.add(x // i)
            if f(i) and f(x // i) and i != (x // i):
                cn += 1
print(cn)
