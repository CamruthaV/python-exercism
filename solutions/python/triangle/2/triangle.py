def is_valid_triangle(sides):
    for side in sides:
        if side <= 0:
            return False
    
    x = sides[0]
    y = sides[1]
    z = sides[2]
    if x+y<=z or y+z<=x or x+z<=y:
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