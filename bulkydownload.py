import requests 
from bs4 import BeautifulSoup 
import os
import argparse


  
def get_file_links(): 
      
    
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
    file_links = [link['href'] for link in links if link['href'].endswith(args.extension)] 
    return file_links,directory 
  
  
def download_file_series(file_links,directory): 
  
    for link in file_links: 
        file_name = link.split('/')[-1]    
  
        print("Downloading file:%s"%file_name)
        os.system('wget '+link+' -P '+directory+'/')
        print("%s downloaded!\n"%file_name) 
  
    print("All Files downloaded!")
    return
  
  

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="for choosing the web url for downloadind the files", required=True)
parser.add_argument("-p", "--path", help="folder path for storing the downloaded files")
parser.add_argument("-e", "--extension", help="for choosing the file extension", required=True)
args = parser.parse_args()

# create response object 
r = requests.get(args.url) 

if r.status_code == 200:
    # getting all video links 
    file_links,directory = get_file_links() 
    # download all videos 
    download_file_series(file_links,directory) 
else:
    print("Please enter the correct web url")  
     
