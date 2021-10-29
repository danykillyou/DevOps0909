import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s,options=Options().add_argument("--disable-extensions"))
driver.maximize_window()

# driver.get("file:///C:/Users/Ofer/OneDrive/%D7%AA%D7%9E%D7%95%D7%A0%D7%95%D7%AA/tip_calc/tip_calc/index.html")
# driver.find_element(By.ID, 'billamt').send_keys('100')
# driver.find_element(By.XPATH,'//*[@id="serviceQual"]/option[3]').click()
# driver.find_element(By.XPATH,'//*[@id="musicqualty"]/option[2]').click()
# driver.find_element(By.XPATH,'/html/body/div/div[1]/input').send_keys("5")
# driver.find_element(By.XPATH,'/html/body/div/div[1]/button').click()
# expected = "9.00"
# actual = driver.find_element(By.XPATH,'/html/body/div/div[2]/span').text
# if expected == actual:
#     print("good")


#2
# webSiteName = driver.title
# print(webSiteName)
# driver.refresh()
# driver.get("https://www.ynet.co.il/")
# webSiteName2 = driver.title
# if webSiteName == webSiteName2:
#     print ("same sites")
# else:
#     print ("different sites")
#3
#the element has the same locators in the other browser

#4
driver.get("https://translate.google.co.il/")
driver.find_element(By.XPATH,"/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div").send_keys("שלום")
#5
driver.get("https://www.youtube.com/")
driver.find_element(By.XPATH,'/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys("רוצה שלום")
time.sleep(0.5)
driver.find_element(By.XPATH,'/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(Keys.ENTER)
# 6
driver.get("https://translate.google.co.il/")
u= driver.find_element(By.XPATH,"/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea")
x=u.tag_name
print(driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea'))
print(u)
print(driver.find_element(By.TAG_NAME,str(x)))

#7
driver.get('https://www.facebook.com/')
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys("username")
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input').send_keys("password",Keys.ENTER)

#8
driver.get("https://www.ynet.co.il")
x=driver.get_cookies()
print(x)
driver.delete_all_cookies()
x=driver.get_cookies()
print(x)
input()

#9

driver.get("https://github.com/")
driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]").send_keys("selenium",Keys.ENTER)
input()
#
#10
# driver = webdriver.Chrome(service=s,options=Options().add_argument("--disable-extensions"))
