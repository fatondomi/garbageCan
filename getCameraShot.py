
import requests

fileName = "newpic.jpg"
ipAdresa = "http://192.168.0.101:4747"

'''
first you open the video feed by running 
    ipAdresa/video?640:480
then you request camera shot with
    ipAdresa/cam/1/frame.jpg
'''
rawImage = requests.get(ipAdresa + "/cam/1/frame.jpg", stream=True)

# save the image received into the file
with open(fileName, 'wb') as fd:
    for chunk in rawImage.iter_content(chunk_size=1024):
        fd.write(chunk)