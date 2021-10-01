
from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
import time
import os

main_url = 'http://course.pcu.ac.kr/report/ubcompletion/progress.php?id=29581'
main_url = 'https://course.pcu.ac.kr/login.php'

"""
options = wd.ChromeOptions()
prefs = {'download.default_directory' : "C:\소중사업\SW공유교육\2021년\수강인원집계\rawdata"}
options.add_experimental_option("prefs", prefs);
driver = wd.Chrome(executable_path='chromedriver.exe', options = options)
"""

driver = wd.Chrome(executable_path='chromedriver.exe')
driver.get(main_url)

driver.find_element_by_id('input-username').send_keys('A03185')

time.sleep(1)
driver.find_element_by_id('input-password').send_keys(os.environ['mypass'])

time.sleep(1)
driver.find_element_by_css_selector('.btn.btn-success').click()  
time.sleep(1)

url_lecture_num = ['29578', '29579', '29580', '29581']

for url_num in url_lecture_num:
    url = 'http://course.pcu.ac.kr/report/ubcompletion/progress.php?id=' + url_num
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_css_selector('.btn.btn-success').click()  
    time.sleep(1)

driver.close()
driver.quit()
