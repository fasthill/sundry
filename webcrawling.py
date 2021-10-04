# https://www.youtube.com/watch?v=7_IEdMv9eFE&t=401s
from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
import requests
import re
import time
import os

headers = {
    'Referer' : 'https://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do'
    # 'User-Agent':
    #  http://useragentstring.com/
    # 'Accept-Language':
}
main_url = 'https://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do'
params = {'currentpage':1, 'rowPerPage': 300}
html = requests.get(main_url, headers= headers)
soup = bs(html.content, 'html.parser')

for idx, tag in enumerate(soup.select('a[href*=jsMemPop]'),1):
    print('[{}] {}'.format(idx,tag.tet))

# #themecast > div.theme_cosoup.select('div#themecast div.theme_head ul.theme_item')nt > div:nth-child(1) > div > ul > li:nth-child(1) > a.theme_info > strong
print('1')

# saved file names = filename
