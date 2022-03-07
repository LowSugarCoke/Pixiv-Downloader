from selenium import webdriver
import requests
import time
import re
from fake_useragent import UserAgent

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)
driver.get('https://www.pixiv.net/ranking.php/') 

ua = UserAgent()
count = 0 
picpath = './data/'

info = re.findall(r'/artworks/\d*',driver.page_source)
info = info[::2]
for url in info:
    print(url)
    print("http://www.pixiv.net"+url)
    r = requests.get("http://www.pixiv.net"+url)
    
    u = re.findall(r'https://i.pximg.net/img-original/img.*?g',r.text)
    
    print(u)
    print(u[0])
    try:
        filename = picpath+"/" + str(count) + ".jpg"       

        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',            
                   'referer':'http://www.pixiv.net%s' % str(url)
                   }     
        r = requests.get(u[0],headers = headers)        
        with open(filename, 'wb') as f:
            f.write(r.content)
            f.close()
        count += 1
        print('this is '+str(count)+'st img')
                        
        time.sleep(0.2)
    except:
        print('failure')


