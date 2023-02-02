from pytube import YouTube, exceptions
from sys import argv
import os

try:
    
    if len(argv) > 1: link = argv[1]
    
    if len(argv) > 2 and os.path.isdir(argv[2]) and os.path.exists(argv[2]): 
        download_location = argv[2]
        print(download_location)
    else: print('Please enter a valid download location')
    
    # use video link provided in command line to create YouTube object
    yt = YouTube(link)
    
    # get yt video by resolution 
    yd = yt.streams.get_by_resolution('720p')
    
    #download video
    yd.download(download_location)
    
except IndexError:
    print("Please provide a video url and try again!")
except exceptions.RegexMatchError:
    print('Please enter a valid url!')

