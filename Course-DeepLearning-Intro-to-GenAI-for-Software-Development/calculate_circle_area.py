#Ask an LLM to write a function that calculates the area of a circle given the radius of that circle.

import math

def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

radius = 5
area = calculate_circle_area(radius)
print("The area of the circle is:", area)

#The area of the circle is: 78.53981633974483