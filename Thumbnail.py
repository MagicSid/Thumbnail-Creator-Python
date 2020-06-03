import os
import shutil
from PIL import Image
DefaultLocation = r"C:\Users\jake\Videos\Dota 2"
DefaultSize = 180,180

def Menu():
    option = 0
    while (option != 1):
        print("""
1 - exit
0 - Create thumbnails
""")
        user = input("Enter your choice: ")
        while user != "0" and user != "1":
            user = input("Enter your choice: ")
        if(user == "0"):
            while(os.path.isdir(user) != True):
                user = input("Enter file directory to scan: ")
            #add size code here if you want users to be able to choose size on thumbnails
            Thumbnail(user,DefaultSize)
        else:
            option = 1
            
        os.system('cls' if os.name == 'nt' else 'clear')

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

Menu()
