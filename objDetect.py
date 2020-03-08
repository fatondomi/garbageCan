
from multiprocessing import Process
from time import sleep
import requests
from PIL import Image 
from PIL import ImageFilter
import io

fileName = "newpic.png"
ipAdresa = "http://192.168.0.101:4747"

def getVideoFeed():
    vidFeed = requests.get(ipAdresa+"/video")

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

def dataAq():
    pilImg = Image.open("newpic.png")
    cpImg = pilImg.crop((0,10,pilImg.width,pilImg.height))
    cpImg.save("cropImage.png")
    

if __name__ == '__main__':

    dataAq()
    '''
    to get a picture you have open the video feed first by running 
        ipAdresa/video?640:480
    then you request camera shot with
        ipAdresa/cam/1/frame.jpg

    helperProcess = Process(target=getVideoFeed,args=())
    helperProcess.daemon = True

    # starting the video feed process
    helperProcess.start()
    sleep(0.1)

    # requests.get returns response object with image
    serverResponse = requests.get(ipAdresa + "/cam/1/frame.jpg", stream=True)

    helperProcess.terminate()

    # we need an io object to create a pil Image 
    # a pil Image can be saved in any format we want png or jpg
    ioObject = io.BytesIO(serverResponse.content)
    pilImg = Image.open(ioObject)

    pilImg.save("newpic.png")
    
    imageWithEdges = pilImg.filter(ImageFilter.FIND_EDGES)
    
    imageWithoutFrame = removeFrame(imageWithEdges)

    imageWithoutFrame.save("picAnalysis.png")
    '''



'''

image.getpixel((x,y)) - ta jep nje pixel touple (r,g,b)
image.putpixel((x,y),(r,g,b)) - e mbishkrun nje pixel

image.size - ta jep nje touple (width,height)

image.width - ta jep nje numer, gjeresine e fotos
image.height - ta jep nje numer, lartesine e fotos

# Find the edges by applying the filter ImageFilter.FIND_EDGES
image.filter(ImageFilter.FIND_EDGES)

# display the new image with edge detection done
image.show()

# Create an image object by reading from the directory given
image = Image.open("./objectExample1.jpg")
'''


