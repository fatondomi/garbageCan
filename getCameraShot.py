
from multiprocessing import Process
from time import sleep
import requests
from PIL import Image
import io

fileName = "newpic.jpg"
ipAdresa = "http://192.168.0.101:4747"

def getVideoFeed():
    vidFeed = requests.get(ipAdresa+"/video")

if __name__ == '__main__':
    '''
    __name tells if the code below is executed or not when this 
     file is imported by other scripts
     
    to get a picture you have open the video feed first by running 
        ipAdresa/video?640:480
    then you request camera shot with
        ipAdresa/cam/1/frame.jpg
    '''

    helperProcess = Process(target=getVideoFeed,args=())
    helperProcess.daemon = True

    # starting the video feed process
    helperProcess.start()
    sleep(0.1)

    # requests.get returns response object
    rawImageJpg = requests.get(ipAdresa + "/cam/1/frame.jpg", stream=True)

    helperProcess.terminate()

    # we need an io object to create a pil Image 
    # a pil Image can be saved in any format we want png or jpg
    ioObject = io.BytesIO(rawImageJpg.content)
    pilImage = Image.open(ioObject)

    pilImage.save(r'newpic.png')



