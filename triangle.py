def is_triangle(sides):
    # Check if the sum of any two sides is greater than or equal to the third side
    return sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]


def equilateral(sides):
    if not is_triangle(sides):
        return False
    
    return len(set(sides)) == 1 if sides[0] > 0 else False
    
        

def isosceles(sides):
    if not is_triangle(sides):
        return False
    
    return len(set(sides)) <= 2 if sides[0] > 0 else False


def scalene(sides):
    if not is_triangle(sides):
        return False
    
    return len(set(sides)) == 3 if sides[0] > 0 else False
