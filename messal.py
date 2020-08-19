import instaloader
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup as BS 
from json import loads
from requests import get
from selenium import webdriver

import sys, os, django
sys.path.append("/") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WEBSITE.settings")
django.setup()
from BLOG.models import posts
def add_posts():
    c=webdriver.Chrome()
    c.get(f'https://www.instagram.com/iamcardib/')
    c.implicitly_wait(10)
    #X1=c.execute_script("window.scrollTo(0, document.body.scrollHeight);var X1=document.body.scrollHeight;return X1;")
    #print(type(X1))
    i=1
    while i<100:
      c.find_element_by_tag_name('body').send_keys(Keys.END)
      i+=1
    
      #c.execute_script("window.scrollTo(0, document.body.scrollHeight)")
      #X1=c.execute_script("window.scrollTo(0, document.body.scrollHeight);var X1=document.body.scrollHeight;return X1;")
      

    images = c.find_elements_by_tag_name('img')
    for image in images:
        #print(type(image.get_attribute('src')))
        a=image.get_attribute('src')
        #username=posts(username=f'{a}')
        a_post = posts(image=f'{a}',username= f'{a}')
        a_post.save()
    #user_posts=c.find_element_by_class_name('_6q-tv')

        
    #username=f'is{user_posts.save_screenshot("_6q-tv")}'
          #print(type(table))
          #print(type(a_post))
          #print(type(a_post))
    
          #z.add(a_post)
          #a_post.save()
        
        # username =pst
        #a_post = posts(username=user_posts)
        #a_post.save()

        


    

if __name__ == "__main__":
  add_posts()



