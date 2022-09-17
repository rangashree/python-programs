import math


def area(r):
    return math.pi*r**2


def circum(r):
    return math.pi*r*2


radius = float(input("circle radius"))

cir_area = area(radius)
cir_circum = circum(radius)

print(cir_area)
print(cir_circum)
