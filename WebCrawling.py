from selenium import webdriver

#크롬 드라이버 설정
driver = webdriver.Chrome('C:\\Users\\ksk98\\PycharmProjects\\chromedriver.exe')

#아주대 포탈 접속
driver.get('https://mportal.ajou.ac.kr/main.do')

driver.find_element_by_xpath('//*[@id="nbHeaderContext"]/div[1]/div[1]/div[1]/ul/li/a').click()

#로그인
driver.find_element_by_xpath('//*[@id="userId"]').send_keys('ksh981214')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('rkdtjsgh12')
driver.find_element_by_xpath('//*[@id="loginSubmit"]').click()

#BB접속
driver.find_element_by_xpath('//*[@id="nbHeaderMenuContext"]/li[3]/em/a').click()


