import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import cookielib
import urllib
import urllib2

driver = webdriver.Firefox()
driver.get('http://172.16.1.186:8080/CADENCIE/servlet/LOGON')
time.sleep(15)
for handle in driver.window_handles:
    driver.switch_to_window(handle)
    print "Switched to handle:", handle
    element = driver.find_element_by_tag_name("form")
    print element.get_attribute("frmLOGON")

bankid = driver.find_element_by_id("idBANK")
bankid.send_keys(01)

empid = driver.find_element_by_id("idEMPLOYEE")
empid.send_keys(200010)

pwdid = driver.find_element_by_id("idPASSWORD")
pwdid.send_keys("Cadencie1")

elem = driver.find_element_by_id("maint")
elem.send_keys(Keys.RETURN)


# print driver.page_source



'''
response = requests.get('http://172.16.1.186:8080/CADENCIE/servlet/LOGON')
time.sleep(15)

f = open('xxx.txt', 'w')
f.write(str(response.text))

'''

'''
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://172.16.1.186:8080/CADENCIE/servlet/LOGON')

print browser.title
print browser.current_url

# browser.quit()
'''

