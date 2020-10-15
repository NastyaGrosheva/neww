from math import*
x = 6.5
while x <= 8:
    y = (x + 2 * x**3 + 1.9)/sqrt(x - 1.5)
    print("{:.1f} {:.6f}".format(x,y))
    x += 0.1