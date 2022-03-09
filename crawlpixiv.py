from selenium import webdriver
import requests
import time
import re
from fake_useragent import UserAgent
import os

#turn on page
# option = webdriver.ChromeOptions()
# option.add_experimental_option("detach",True)
# driver = webdriver.Chrome(options=option)
# driver.get('https://www.pixiv.net/ranking.php/') 

web_page =  requests.get('https://www.pixiv.net/ranking.php/')

if web_page!=200:
    print("error")


#Get date
date = re.findall(r'\[\w+\.\w+\.\w+\]',web_page.text)
date = date[0]
date = date.strip('[').strip(']')
print(date)

os.makedirs("./data/"+date, exist_ok=True)

# ua = UserAgent()
count = 0 
picpath = './data/'+date

#Get image name
name = re.findall(r'"noopener">.*?>',web_page.text)
name=name[1:51]
for i in range(0,len(name)):
    name[i] = name[i].strip('"noopener">').strip('</a>')
print(name)


# Get image url
info = re.findall(r'/artworks/\d*',web_page.text)
info = info[::2]
for url in info:
    print(url)
    print("http://www.pixiv.net"+url)
    
    #Get big size image url
    r = requests.get("http://www.pixiv.net"+url)
    u = re.findall(r'https://i.pximg.net/img-original/img.*?g',r.text)
    
    print(u)
    print(u[0])
    try:
        filename = picpath+"/" + "#"+str(count+1)+" "+str(name[count]) + ".jpg"       

        #fake agent
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',            
                   'referer':'http://www.pixiv.net%s' % str(url)
                   }   
        
        #download image  
        r = requests.get(u[0],headers = headers)        
        with open(filename, 'wb') as f:
            f.write(r.content)
            f.close()
        count += 1
        print('this is '+str(count)+'st img')
                        
        time.sleep(0.2)
    except:
        print('failure')


