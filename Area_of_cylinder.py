#This program calculates the area of a cylinder.
height = float(input('Enter value of height: '))
radius = float(input('Enter value of radius: '))
Area_of_cylinder = (2 * 3.14159 * radius**2) + (2* 3.14159 * radius * height)
print('The area of a cylinder with height %s and radius %s is %s' % (height, radius, Area_of_cylinder))
