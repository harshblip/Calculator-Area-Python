import math
pi = math.pi

def circle(radius):
    return pi * radius ** 2

def cube(side):
    return side ** 3

def cylinder(radius, height):
    return 2 * pi * radius + 2 * pi * height

def sphere(radius):
    return 2 * pi * (radius ** 2)

print("Enter 1 for Circle, 2 for Cube, 3 for Cylinder, 4 for Sphere")
val = int(input())

if val == 1:
    r = float(input("Enter radius of circle: "))
    print(circle(r))
elif val == 2:
    s = float(input("Enter side of Cube: "))
    print(cube(s))
elif val == 3:
    rad = float(input("Enter radius of cylinder: "))
    h = float(input("Enter the height of cylinder: "))
    print(cylinder(rad, h))
elif val == 4:
    radius = float(input("Enter radius of sphere: "))
    print(radius)

