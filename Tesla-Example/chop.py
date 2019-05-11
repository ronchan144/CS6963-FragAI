from PIL import Image

infile = '1.jpg'

img = Image.open(infile)
width, height = img.size

val = input("Type the percentage: ")
try:
    if "." in val :
        percentage = float(val)
    else:
        percentage = int(val)
except ValueError:
    print("The input was not a number")

print( "Percentage is ",percentage)
type(percentage)

chopsize = int(percentage * height)

box = (0, 0, width -1, chopsize)

print ('%s %s' % (infile, box))

img.crop(box).save('zchop.jpg')
