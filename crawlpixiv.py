from selenium import webdriver
import requests
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=option)
driver.get('https://www.pixiv.net/ranking.php/') 

member_button = driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/div/a[2]')
member_button.click()

acount = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/form/div[1]/div[1]/input')
acount.send_keys('jack20499@yahoo.com.tw')

password = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/form/div[1]/div[2]/input')
password.send_keys('7SgfqAPfH3TetuM')

submit = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/form/button')
submit.click()

time.sleep(10)
image_link_data=driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[3]/div[1]/section[1]/div[2]/a')
# image_link = image_link_data.get_property('href')
print(image_link_data.text)