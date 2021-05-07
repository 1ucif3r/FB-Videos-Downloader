import os
from datetime import datetime
from tqdm import tqdm
import requests,re,sys

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'

color_random=[color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END]

os.system('cls')
logo = color.OKGREEN +"""

        ███████  █████   ██████ ███████ ██████   ██████   ██████  ██   ██ 
        ██      ██   ██ ██      ██      ██   ██ ██    ██ ██    ██ ██  ██  
        █████   ███████ ██      █████   ██████  ██    ██ ██    ██ █████   
        ██      ██   ██ ██      ██      ██   ██ ██    ██ ██    ██ ██  ██  
        ██      ██   ██  ██████ ███████ ██████   ██████   ██████  ██   ██ 
                                                                                         
                         #### VIDEOS DOWNLOADER ####

"""
print (logo)
print(color.RED + "               [$] Coded By  : Hritik Kumbhar(th31ucif3r) "+ color.END)
print(color.RED + "               [$] Example   : https://www.facebook.com/user/videos/xxxxxxxxxx"+ color.END)
def memek():
    try:
                bau = str(input("\n  [!] Select Resolution\n\n  1. HD (High Definition)\n  2. SD (Standard Definition)\n\n  [$] ~# ")).upper()
                if bau == '1':
                    print("")
                    video_url = re.search(r'hd_src:"(.+?)"', html).group(1)
                    file_size_request = requests.get(video_url, stream=True)
                    file_size = int(file_size_request.headers['Content-Length'])
                    block_size = 1024 
                    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                    with open(filename + '.mp4', 'wb') as f:
                        for data in file_size_request.iter_content(block_size):
                            t.update(len(data))
                            f.write(data)
                    t.close()
                    print("\n[!] Download Successfully") 
                    sys.exit(0)  

                if bau == '2':
                    print("")
                    video_url = re.search(r'hd_src:"(.+?)"', html).group(1)
                    file_size_request = requests.get(video_url, stream=True)
                    file_size = int(file_size_request.headers['Content-Length'])
                    block_size = 1024 
                    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                    with open(filename + '.mp4', 'wb') as f:
                        for data in file_size_request.iter_content(block_size):
                            t.update(len(data))
                            f.write(data)
                    t.close()
                    print("\n[!] Download Successfully")
                    sys.exit(0)


    except(KeyboardInterrupt):
        print(color.WARNING +"\n[!] Error ! Try Again"+ color.END)

try:
    while True:        
        url = input("\n  [URL] ~# ")
        x = re.match(r'^(https:|)[/][/]www.([^/]+[.])*facebook.com', url)

        if x:
            html = requests.get(url).content.decode('utf-8')
        else:
            print(color.WARNING +"\n[!] Error ! Try Again"+ color.END)
            sys.exit(0)

        _qualityhd = re.search('hd_src:"https', html)
        _qualitysd = re.search('sd_src:"https', html)
        _hd = re.search('hd_src:null', html)
        _sd = re.search('sd_src:null', html)

        list = []
        _thelist = [_qualityhd, _qualitysd, _hd, _sd]
        for id,val in enumerate(_thelist):
            if val != None:
                list.append(id)

        memek()

except KeyboardInterrupt:
    print("\n[!] Error ")
    
