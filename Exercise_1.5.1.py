print 'This is a program to compute the volume of a cube. Please enter the dimensions.\n'
try:
    width = raw_input('Width: ')
    width = float(width)
    length = raw_input('Length: ')
    length = float(length)
    height = raw_input('Height: ')
    height = float(height)
    volume = width * length * height
    print '\n The Volume of the cube is', volume, '\n'
except:
    print 'Please enter a number\n'
