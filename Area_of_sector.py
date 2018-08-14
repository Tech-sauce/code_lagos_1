#This program calculates the area of a sector.
angle = float(input('Enter angle in degrees: '))
radius = float(input('Enter radius: '))
Area_of_sector = (angle / 360) * (3.14159 * radius**2)
print('The area of a sector with angle %s and radius %s is %s' % (angle, radius, Area_of_sector))
