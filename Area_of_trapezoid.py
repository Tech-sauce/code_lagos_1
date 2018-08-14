#This program calculates the area of a trapezoid.
base_1 = float(input('Enter the length of first base: '))
base_2 = float(input('Enter the length of second base: '))
height = float(input('Enter the value of height: '))
Area_of_trapezoid = ((base_1 + base_2) / 2) * height
print('The area of a trapezoid with bases %s , %s and height %s is %s' % (base_1, base_2, height, Area_of_trapezoid))
