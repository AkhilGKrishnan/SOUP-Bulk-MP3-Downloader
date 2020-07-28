
import requests 
from bs4 import BeautifulSoup 
import os
  

# specify the URL of the archive here 
archive_url = "http://kumarmp3.com/?page_id=63/"
  
def get_video_links(): 
      
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
  
  
def download_video_series(video_links,directory): 
  
    for link in video_links: 
  
        '''iterate through all links in video_links 
        and download them one by one'''
          
        # obtain filename by splitting url and getting  
        # last string
        print(link) 
        file_name = link.split('/')[-1]    
  
        print("Downloading file:%s"%file_name)

        os.system('wget '+link+' -P '+directory+'/')
          
        """ # create response object 
        r = requests.get(link) 
          
        # download started 
        with open(file_name, 'wb') as f: 
            f.write(r.content)  """
          
        print("%s downloaded!\n"%file_name) 
  
    print("All videos downloaded!")
    return
  
  
if __name__ == "__main__": 
  
    # getting all video links 
    video_links,directory = get_video_links() 
  
    # download all videos 
    download_video_series(video_links,directory) 
     
