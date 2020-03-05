
from multiprocessing import Process
from time import sleep
import requests

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

    rawImage = requests.get(ipAdresa + "/cam/1/frame.jpg", stream=True)

    helperProcess.terminate()

    # save the image received into the file
    with open(fileName, 'wb') as fd:
        for chunk in rawImage.iter_content(chunk_size=1024):
            fd.write(chunk)