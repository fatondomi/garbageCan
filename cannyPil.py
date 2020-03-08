
from PIL import Image
from PIL import ImageFilter

def removeFrame(imageIn):
    # the frame is actually an edge the edge filter marks down
    #  it consists of a 1 pixel width of the perimeter of the function 
    limX = imageIn.width - 1
    limY = imageIn.height - 1

    for i in range(imageIn.width):
        imageIn.putpixel((i,0),(0,0,0))
        imageIn.putpixel((i,limY),(0,0,0))
        
    for i in range(imageIn.height):
        imageIn.putpixel((0,i),(0,0,0))
        imageIn.putpixel((limX,i),(0,0,0))

    return imageIn

# Create an image object
image = Image.open("./objectExample1.jpg")

imageWithEdges = image.filter(ImageFilter.FIND_EDGES)

imageWithoutFrame = removeFrame(imageWithEdges)

imageWithoutFrame.show()

'''

image.getpixel((x,y)) - ta jep nje pixel touple (r,g,b)
image.putpixel((x,y),(r,g,b)) - e mbishkrun nje pixel


# Find the edges by applying the filter ImageFilter.FIND_EDGES
imageWithEdges = image.filter(ImageFilter.FIND_EDGES)

# display the new image with edge detection done
imageWithEdges.show()
'''
