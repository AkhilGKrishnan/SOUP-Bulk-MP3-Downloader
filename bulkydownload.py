import requests 
from bs4 import BeautifulSoup 
import os
import argparse


  
def get_Audio_links(): 
      
    # create response object 
    r = requests.get(archive_url) 
    # create beautiful-soup object 
    soup = BeautifulSoup(r.content,'html5lib') 
    # find all links on web-page 
    links = soup.findAll('a')
    
    # Folder for storing the downloaded file
    if args.path:
        directory = args.path
    else:    
        directory = soup.title.text
        directory = directory.replace(" ", "_")
        os.system('mkdir '+directory+'') 
        
    # filter the link sending with .mp4 
    file_links = [link['href'] for link in links if link['href'].endswith('mp3')] 
    return file_links,directory 
  
  
def download_file_series(file_links,directory): 
  
    for link in file_links: 
        file_name = link.split('/')[-1]    
  
        print("Downloading file:%s"%file_name)
        os.system('wget '+link+' -P '+directory+'/')
        print("%s downloaded!\n"%file_name) 
  
    print("All videos downloaded!")
    return
  
  

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="for choosing the web url for downloadind the files")
parser.add_argument("-p", "--path", help="folder path for storing the downloaded files")
args = parser.parse_args()
if args.url:
    # specify the URL of the archive here 
    archive_url = args.url
    # getting all video links 
    file_links,directory = get_Audio_links() 
    # download all videos 
    download_file_series(file_links,directory) 
else:
    print("enter the web url")    
     
