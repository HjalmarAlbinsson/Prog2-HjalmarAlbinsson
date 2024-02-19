for a in range(1, 1000):
    for b in range(a, 1000):
        if (a**2 + b**2)**0.5 + a + b == 1000 and (a**2 + b**2)**0.5 > b:
            print(1000*a*b - (a**2)*b - (b**2)*a)