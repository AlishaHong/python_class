#크롤링 실습


import requests
from bs4 import BeautifulSoup

url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

response = requests.get(url)
print(response.status_code)
print(response)

# if response.status_code == 200:
#     html = response.text
#     # print(html)
#     soup = BeautifulSoup(html, 'html.parser')
#     print(soup)

# else : 
#     print(response.status_code)


url = "https://search.naver.com/search.naver?ssc=tab.kin.kqna&where=kin&sm=tab_jum&query=%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4"

response = requests.get(url)
print(response)


    
html = response.text
soup = BeautifulSoup(html, 'html.parser')
# a = soup.select_one('#newsstand > div.MediaView-module__media_area___Z4js3 > div:nth-child(1) > ul > li:nth-child(1) > div > a')
# title = soup.select('#newsstand > div.MediaView-module__media_area___Z4js3 > div:nth-child(1) > ul > li:nth-child(1) > div > a')[0].get_text(strip=True)
title2= soup.select_one('#main_pack > section.sc_new.sp_nkin._fe_kin_collection > div.api_subject_bx > ul > li:nth-child(2) > div > div.question_area > div:nth-child(3) > a').get_text(strip=True)
print(title2)
# if title2:
#     title1 = title2.get_text(strip=True)
#     print(title1)
# else:
    # print("첫 번째 요소를 찾을 수 없습니다.")


#main_pack > section.sc_new.sp_nkin._fe_kin_collection > div.api_subject_bx > ul > li:nth-child(2) > div > div.question_area > div:nth-child(3) > a
#main_pack > section.sc_new.sp_nkin._fe_kin_collection > div.api_subject_bx > ul > li:nth-child(2) > div > div.question_area > div:nth-child(3) > a