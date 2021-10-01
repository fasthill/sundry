#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
import time
import os


# In[2]:


main_url = 'http://course.pcu.ac.kr/report/ubcompletion/progress.php?id=29581'
main_url = 'https://course.pcu.ac.kr/login.php'


# In[3]:


"""
options = wd.ChromeOptions()
prefs = {'download.default_directory' : "C:\소중사업\SW공유교육\2021년\수강인원집계\rawdata"}
options.add_experimental_option("prefs", prefs);
driver = wd.Chrome(executable_path='chromedriver.exe', options = options)
"""


# In[4]:


driver = wd.Chrome(executable_path='chromedriver.exe')


# In[5]:


driver.get(main_url)


# In[6]:


driver.find_element_by_id('input-username').send_keys('A03185')


# In[7]:


time.sleep(1)
driver.find_element_by_id('input-password').send_keys(os.environ['mypass'])


# In[8]:


time.sleep(1)
driver.find_element_by_css_selector('.btn.btn-success').click()  
time.sleep(1)


# In[9]:


url_lecture_num = ['29578', '29579', '29580', '29581']


# In[10]:


for url_num in url_lecture_num:
    url = 'http://course.pcu.ac.kr/report/ubcompletion/progress.php?id=' + url_num
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_css_selector('.btn.btn-success').click()  
    time.sleep(1)


# In[11]:


driver.close()
driver.quit()


# In[ ]:




