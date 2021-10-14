from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
import time
import os

# !pip install chromedriver_autoinstaller

import chromedriver_autoinstaller

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path
                                      
main_url = 'https://course.pcu.ac.kr/login.php'

driver = wd.Chrome()
driver.set_window_position(-10000,0) # hide windows
driver.get(main_url)

driver.find_element_by_id('input-username').send_keys('A03185')

time.sleep(1)
driver.find_element_by_id('input-password').send_keys(os.environ['mypass'])

time.sleep(1)
driver.find_element_by_css_selector('.btn.btn-success').click()  
time.sleep(1)

url_lecture_num = ['29578', '29579', '29580', '29581']

Initial_path = "C:/Users/user/Downloads"
filename = []

for url_num in url_lecture_num:
    url = 'http://course.pcu.ac.kr/report/ubcompletion/progress.php?id=' + url_num
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_css_selector('.btn.btn-success').click()  
    time.sleep(1)
    filename.append(max([os.path.join(Initial_path, f) for f in os.listdir(Initial_path)], key=os.path.getctime))

driver.close()
driver.quit()

# saved file names = filename
