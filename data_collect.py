from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import time

PATH = '/home/shreyank99/Desktop/grass_indentifier/grass_indentifier/Selenium_Webdrivers/chromedriver'
driver = webdriver.Chrome(executable_path=PATH)
driver.get('https://www.google.com')
driver.maximize_window()

search_box = driver.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
search_box.click()
search_box.send_keys('Kentucky Bluegrass yard')
search_box.send_keys(Keys.RETURN)

images = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[3]/div/div/div[1]/div/div/div[1]/div/div[2]/a')
images.click()
while(len(driver.find_elements_by_tag_name('img')) <= 500):
	load_more = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input')
	if(load_more.is_displayed() == False):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
		time.sleep(3)
	else:
		load_more.click()

images_elements = driver.find_elements_by_tag_name('img')
images_src = []

for image in images_elements:
    images_src.append((image.get_attribute('src')))

print(len(set(images_src)))
driver.close()

count = 1
for src in set(images_src):
	if(src != None):
		# print(src)
		urllib.request.urlretrieve(src, "./grass_data/kentucky_bluegrass/Bluegrass{}.jpg".format(count))
		count += 1
