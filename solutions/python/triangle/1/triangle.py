def is_valid_triangle(sides):
    for side in sides:
        if side <= 0:
            return False
    
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a+b<=c or b+c<=a or a+c<=b:
        return False
    return True

def equilateral(sides):
    if not is_valid_triangle(sides):
        return False
    if sides[0] == sides[1] == sides[2]:
        return True
    return False

def isosceles(sides):
    if not is_valid_triangle(sides):
        return False
    if sides[0]==sides[1] or sides[1]==sides[2] or sides[0]==sides[2]:
        return True
    return False


def scalene(sides):
    if not is_valid_triangle(sides):
        return False
    if sides[0]==sides[1] or sides[1]==sides[2] or sides[0]==sides[2]:
        return False
    return True