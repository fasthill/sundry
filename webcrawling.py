# https://www.youtube.com/watch?v=7_IEdMv9eFE&t=401s
from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
import requests
import re
import time
import os

main_url = 'https://www.assembly.go.kr/assm/memact/congressman/memCond/memCond.do'

html = requests.get(main_url)
soup = bs(html.content, 'html.parser')

list_ = soup.select('a[href*=jsMemPop]')
# list_ = soup.select('a', {'href': re.compile(r'jsMemPop')})

# #themecast > div.theme_cosoup.select('div#themecast div.theme_head ul.theme_item')nt > div:nth-child(1) > div > ul > li:nth-child(1) > a.theme_info > strong
print('1')

# saved file names = filename
