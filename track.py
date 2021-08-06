from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.command import Command
import urllib.request

import time
import re
import boto3

links = ["https://www.facebook.com/photo.php...."]


chrome_options = Options()
# chrome_options.add_argument("--headless")        
chrome_options.add_argument("--log-level=3")
#configurando o user-agent
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135")
chrome_options.add_argument("--disable-dev-shm-usage")

def execute():
  driver = webdriver.Chrome(options=chrome_options)

  for i, link in enumerate(links):
    driver.get(link)
    time.sleep(1)
    image = driver.find_element_by_class_name('gitj76qy').get_attribute('src')
    download_image(image, i)
    print('aqui')


def download_image(url, i):
  urllib.request.urlretrieve(url, f'images/{i}.jpg') 


execute()

