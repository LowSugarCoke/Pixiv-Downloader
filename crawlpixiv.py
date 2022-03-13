import requests
import time
import re
import os
from tqdm import tqdm

url = 'https://www.pixiv.net/ranking.php/'

#turn on page
web_page =  requests.get(url)

if web_page.status_code==200:
    print("Connect url",url)
    #Get date
    date = re.findall(r'\[\w+\.\w+\.\w+\]',web_page.text)
    date = date[0]
    date = date.strip('[').strip(']')
    
    #Create folder if not exist
    os.makedirs("./data/"+date, exist_ok=True)

    #Get image name
    name = re.findall(r'"noopener">.*?>',web_page.text)
    name=name[1:51]
    #remove reducant symbol and replace illegal symbol of file name
    for i in range(0,len(name)):
        name[i] = name[i].strip('"noopener">').strip('</a>')
        name[i] = name[i].replace('/','.').replace('\\','.').replace('*','.').replace(':','.').replace('?','.').replace('"','.').replace('<','.').replace('>','.').replace('|','.')
    
    # Get image url
    info = re.findall(r'/artworks/\d*',web_page.text)
    info = info[::2]
    
    count = 0 
    picpath = './data/'+date
    progress = tqdm(total=50)
    for url in info:
        progress.update(1)
        
        #Get big size image url
        r = requests.get("http://www.pixiv.net"+url)
        u = re.findall(r'https://i.pximg.net/img-original/img.*?g',r.text)
        
        if(r.status_code==200):        
            try:
                filename = picpath+"/" + "#"+str(count+1)+" "+str(name[count]) + ".jpg"     
                # print(filename)

                #fake agent
                headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',            
                        'referer':'http://www.pixiv.net%s' % str(url)
                        }   
                
                #download image  
                r = requests.get(u[0],headers = headers)        
                with open(filename, 'wb') as f:
                    f.write(r.content)
                    f.close()                            
                time.sleep(0.2)
            except:
                print('download image failure',str(count+1)+" "+str(name[count]))
        else:
            print("Cannot connect url","http://www.pixiv.net"+url)
        count += 1
else:
    print("Cannot connect url",url)
