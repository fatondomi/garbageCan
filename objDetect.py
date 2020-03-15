
from multiprocessing import Process
from time import sleep
from time import thread_time
import requests
from PIL import Image 
from PIL import ImageFilter
import io
import efficiently

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

def getColor(rgbPixel):

    red = rgbPixel[2]
    green = rgbPixel[1]
    blue = rgbPixel[0]

    # white gray black constant when r g b values are close together
    # it determines wheather it is a color or not
    wgbK = 20
    dif1 = abs(red - green)
    dif2 = abs(blue - green)
    if(dif1<wgbK and dif2<wgbK):
        if((red+green+blue)>320):
            #return white
            return (255,255,255)
        else:
            #return black
            return (0,0,0)

    # color konstant
    colorK = 2
    #checking for red
    if(red > blue*colorK and red > green*colorK):
        #return red
        return (255,0,0)

    #checking for green
    if(green > blue*colorK and green > red*colorK):
        #return green
        return (0,255,0)

    #checking for blue
    if(blue > red*colorK and blue > green*colorK):
        #return blue
        return (0,0,255)

    #checking for yellow
    if(blue*colorK < red and blue*colorK < green):
        #return yellow
        return (255,255,0)

    #checking for magenta
    if(green*colorK < red and green*colorK < blue):
        #return magenta
        return (255,0,255)

    #checking for cyan
    if(red*colorK < green and red*colorK < blue):
        #return cyan
        return (0,255,255)
    
    return (255,255,255)

colorGraph = efficiently.filter(0,255,3,getColor)

if __name__ == '__main__':
    print("Color graph ready after: {} seconds".format(thread_time())) 

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
    '''

    pngImg = Image.open("newpic.png")
    
    #croping image
    cpImg = pngImg.crop((0,15,pngImg.width,pngImg.height))
    #cpImg.save("cropImage.png")

    # filtering the image for colors
    for r in range(cpImg.width):
        for c in range(cpImg.height):
            pxl = cpImg.getpixel((r,c))
            cpImg.putpixel((r,c),colorGraph[pxl[0]][pxl[1]][pxl[2]])
    
    cpImg.save("simpleImage.png")

    imageWithEdges = cpImg.filter(ImageFilter.FIND_EDGES)
    imageWithoutFrame = removeFrame(imageWithEdges)

    imageWithoutFrame.save("picAnalysis.png")



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

def dataAq():
    print("Color graph ready after: {} seconds".format(thread_time())) 
    pilImg = Image.open("newpic.png")
    cpImg = pilImg.crop((0,15,pilImg.width,pilImg.height))
    cpImg.save("cropImage.png")

    for r in range(cpImg.width):
        for c in range(cpImg.height):
            pxl = cpImg.getpixel((r,c))
            cpImg.putpixel((r,c),colorGraph[pxl[0]][pxl[1]][pxl[2]])
    
    cpImg.save("simpleImage.png")

    imageWithEdges = cpImg.filter(ImageFilter.FIND_EDGES)
    imageWithoutFrame = removeFrame(imageWithEdges)

    imageWithoutFrame.save("picAnalysis.png")
'''


