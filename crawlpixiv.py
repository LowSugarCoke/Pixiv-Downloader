import requests
import time
import re
from fake_useragent import UserAgent
import os
from tqdm import tqdm, trange

#turn on page
web_page =  requests.get('https://www.pixiv.net/ranking.php/')


#Get date
date = re.findall(r'\[\w+\.\w+\.\w+\]',web_page.text)
date = date[0]
date = date.strip('[').strip(']')
# print(date)

os.makedirs("./data/"+date, exist_ok=True)

#Get image name
name = re.findall(r'"noopener">.*?>',web_page.text)
# print(name)
name=name[1:51]
for i in range(0,len(name)):
    name[i] = name[i].strip('"noopener">').strip('</a>')
# print(name)

count = 0 
picpath = './data/'+date
progress = tqdm(total=50)


# Get image url
info = re.findall(r'/artworks/\d*',web_page.text)
info = info[::2]
for url in info:
    progress.update(1)
    
    # print(url)
    # print("http://www.pixiv.net"+url)
    
    #Get big size image url
    r = requests.get("http://www.pixiv.net"+url)
    u = re.findall(r'https://i.pximg.net/img-original/img.*?g',r.text)
    
    # print(u)
    # print(u[0])
    try:
        filename = picpath+"/" + "#"+str(count+1)+" "+str(name[count].strip("//")) + ".jpg"     
        print(filename)

    #     #fake agent
    #     headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',            
    #                'referer':'http://www.pixiv.net%s' % str(url)
    #                }   
        
    #     #download image  
    #     r = requests.get(u[0],headers = headers)        
    #     with open(filename, 'wb') as f:
    #         f.write(r.content)
    #         f.close()
    # #     print('this is '+str(count)+'st img')
                        
    #     time.sleep(0.2)
    except:
        print('failure')
    count += 1
