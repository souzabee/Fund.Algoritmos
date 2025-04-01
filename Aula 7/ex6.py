from math import sqrt
def eq(x, y, z):
    calc = sqrt(x) + sqrt(y) + sqrt(z) + (x + y) / 2 + (y + z) / 2 + (x + z) / 2
    return calc
print(eq(5, 4, 2))