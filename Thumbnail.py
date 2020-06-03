import os
import shutil
from PIL import Image
DefaultLocation = r"C:\Users\jake\Videos\Dota 2"
DefaultSize = 180,180



def Thumbnail(location,size):
    ThumbnailLocation = location + r"\Thumbnails"
    if(os.path.isdir(ThumbnailLocation) == True):
        shutil.rmtree(ThumbnailLocation)
    os.mkdir(ThumbnailLocation)
    files = os.listdir(location)
    for entry in files:
        if(entry.lower().endswith((".png",".jpg",".jpeg"))):
            print(entry)
            CreateThumbnail(location + "\\" + entry,size,ThumbnailLocation)
    
    if(os.path.isdir(ThumbnailLocation) != True and False):
        os.rmdir(ThumbnailLocation)
    
    input("Press Enter to Finish")

def CreateThumbnail(imageloc,size,newLoc):
    im = Image.open(imageloc)
    im.thumbnail(size,Image.ANTIALIAS)
    im.save(newLoc + "\\" + os.path.basename(imageloc))

Thumbnail(DefaultLocation,DefaultSize)
