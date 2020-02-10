def add(list):
    x = 0
    for num in list:
        x += num
    return x

def multiply(list):
    x = 1
    for num in list:
        x = x*num
    return x

def subtract(list):
    x= list[0]
    length = len(list)
    y = 1
    while y != length:
        x -= list[y]
        y += 1
    return x

def divide(list):
    x= list[0]
    length = len(list)
    y = 1
    while y != length:
        x = x / list[y]
        y += 1
    return x

def area_of_circle(radius):
    return multiply([3.14,radius,radius])

def area_of_square(length1,length2):
    return multiply([length1,length2])

def area_of_triangle(base,height):
    return multiply([base,height,0.5])

