
from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 
   
# For using listdir() 
import os 
   
  
# Below code does the authentication 
# part of the code 
gauth = GoogleAuth() 
  
# Creates local webserver and auto 
# handles authentication. 
gauth.LocalWebserverAuth()        
drive = GoogleDrive(gauth) 
   
# replace the value of this variable 
# with the absolute path of the directory 
path = os.path.expanduser("~/Desktop/setup/") #Correct it if you use on other setup
# iterating thought all the files/folder 
# of the desired directory 
if 'data.csv' in os.listdir(path): 
   
    f = drive.CreateFile({'title': 'data.csv'}) 
    f.SetContentFile(os.path.join(path, 'data.csv')) 
    f.Upload() 
  
    # Due to a known bug in pydrive if we  
    # don't empty the variable used to 
    # upload the files to Google Drive the 
    # file stays open in memory and causes a 
    # memory leak, therefore preventing its  
    # deletion 
    f = None
