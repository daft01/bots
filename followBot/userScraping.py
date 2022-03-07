from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')

username = "mijuwumijil"
password = "Test0816"

time.sleep(3)

driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, '[type=submit]').click()

time.sleep(3)

if "Save Your Login Info?" in driver.page_source:
	driver.find_element(By.CSS_SELECTOR, '[type=button]').click()
	time.sleep(3)

if "Turn on Notifications" in driver.page_source:
	driver.find_element_by_xpath('//button[text()="Not Now"]').click()
	time.sleep(3)

driver.get('https://www.instagram.com/insomniacevents/')

time.sleep(3)

tags = driver.find_elements(By.TAG_NAME, 'a')

for tag in tags:
	if tag.get_attribute("href") == "https://www.instagram.com/insomniacevents/followers/":
		tag.click()
		time.sleep(2)

# element for the scroll follow modal. it might change in the future
scrollElm = "oMwYe"
actions = ActionChains(driver)

for x in range(5):
	try:
		# element for the scroll follow modal. it might change in the future
		oMwYe = driver.find_element_by_class_name(scrollElm)
		actions.move_to_element(oMwYe).perform()
		time.sleep(.2)
	except:
  		print("users didn't load fast enough to scroll")

elements = driver.find_elements(By.CSS_SELECTOR, '[data-testid=user-avatar]')


f = open("demofile2.txt", "a")

for element in elements:
	print(element.get_attribute("alt").split("'")[0])
	f.write(element.get_attribute("alt").split("'")[0] + "\n")

f.close()

# for tag in tags:
# 	print(tag.get_attribute("class"))