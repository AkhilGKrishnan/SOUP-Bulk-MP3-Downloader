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
   
    directory = soup.title.text
    directory = directory.replace(" ", "_")
    print(directory) 
    os.system('mkdir '+directory+'') 
  
    # filter the link sending with .mp4 
    video_links = [link['href'] for link in links if link['href'].endswith('mp3')] 
    
  
    return video_links,directory 
  
  
def download_Audio_series(video_links,directory): 
  
    for link in video_links: 
        file_name = link.split('/')[-1]    
  
        print("Downloading file:%s"%file_name)
        os.system('wget '+link+' -P '+directory+'/')
        print("%s downloaded!\n"%file_name) 
  
    print("All videos downloaded!")
    return
  
  

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="for selecting the bulk audio web url")
args = parser.parse_args()
if args.url:
    # specify the URL of the archive here 
    archive_url = args.url
    # getting all video links 
    video_links,directory = get_Audio_links() 

    # download all videos 
    download_Audio_series(video_links,directory) 
     
