from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 크롬 드라이버 설정
driver = webdriver.Chrome('C:\\Users\\ksk98\\PycharmProjects\\chromedriver.exe')
driver.implicitly_wait(3)
# 로그인 bb 접속
driver.get('https://eclass2.ajou.ac.kr/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1')
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="userId"]').send_keys('ksh981214')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('rkdtjsgh12')
driver.find_element_by_xpath('//*[@id="loginSubmit"]').click()

try:
     element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID,'_3_1termCourses__19_1')))
finally:
     pass

html = driver.find_element_by_xpath('//*[@id="_3_1termCourses__19_1"]/ul').get_attribute('innerHTML')
soup = bs(html, 'html.parser')
course_list_raw = soup.find_all('a', href=True)
course_list = []
course_detail_base = 'https://eclass2.ajou.ac.kr/webapps/blackboard/execute/announcement?method=search&context=mybb&course_id='
course_detail_list = []
for i in course_list_raw:
     course_each_id = str(i).split('id=')[1].split('&amp')[0]
     course_list.append(course_each_id)
     course_each_url = course_detail_base + course_each_id
     course_detail_list.append([course_each_url])

for i in course_detail_list:
      driver.get(i[0])
      try:
           element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID,'courseMenuPalette_contents')))

           # 공지사항

           announce_raw = driver.page_source
           soup = bs(announce_raw, 'html.parser')
           announcements = soup.select('li.clearfix')[17:]
           announcements.reverse()

           for ann in announcements:
                print(ann.attrs['id'])
                print(ann.text)
                print('-----------------------------')

           # contents
           homework_html = driver.find_element_by_xpath('//*[@id="courseMenuPalette_contents"]').get_attribute('innerHTML')
           soup = bs(homework_html, 'html.parser')
           nav_bars = soup.find_all('a')
           for bar in nav_bars:
                #과제
                if str(bar.find('span').text) == '과제출제/제출' or str(bar.find('span').text) == 'Assignments':
                     homework_url = 'https://eclass2.ajou.ac.kr' + str(bar['href'])
                     i.append(homework_url)
                     driver.get(homework_url)
                     homework_raw = driver.page_source
                     soup = bs(homework_raw, 'html.parser')
                     homeworks = soup.select('ul.contentList > li')
                     for home in homeworks:
                            print(home.attrs['id'])
                            print(home.text)
                            print('-------------------------------------')
                #강의노트
                if str(bar.find('span').text) == '강의노트':
                     classnote_url = 'https://eclass2.ajou.ac.kr' + str(bar['href'])
                     i.append(classnote_url)
                     driver.get(classnote_url)
                     classnote_raw = driver.page_source
                     soup = bs(classnote_raw, 'html.parser')
                     classnotes = soup.select('ul.contentList > li')
                     for classnote in classnotes:
                          print(classnote.attrs['id'])
                          print(classnote.text)
                          print('----------------------------------------')

      except Exception as e:
            homework_html = None
            print('error')
            pass


