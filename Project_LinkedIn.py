from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import csv
import os


options = Options()
#options.headless = True

options.add_argument("--no-sandbox")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument("--start-maximized")
options.add_argument('--ignore-certificate-errors')
options.add_argument('user-data-dir="/home/tarek/Selenium_Projects/Project_LinkedIn/user_dir"')


driver=webdriver.Chrome(options=options, executable_path='/home/practice_environment/chromedriver')

driver.get('https://www.linkedin.com/home')
time.sleep(4)
try:
	sign_in_button=driver.find_element_by_xpath("//a[@class='nav__button-secondary']")
	sign_in_button.click()
	time.sleep(4)
	email_form=driver.find_element_by_id('username')
	email_form.send_keys('md.tarek00009@gmail.com')
	pass_form=driver.find_element_by_id('password')
	pass_form.send_keys('D0ntforgetme')
	sign_in_submit=driver.find_element_by_tag_name('button')
	sign_in_submit.click()
	time.sleep(15)
	print(driver.current_url)

except:
	driver.get('https://www.linkedin.com/company/the-right-hand-task-force/')
	company_name=driver.find_element_by_xpath('//*[@id="ember52"]//h1/span').text
	print(company_name)
	employee_count=driver.find_element_by_xpath('//span[@class="link-without-visited-state t-bold t-black--light"]').text
	print(employee_count)
	company_industry=driver.find_element_by_xpath('//div[@class="org-top-card-summary-info-list__info-item"]').text
	print(company_industry)
	followers=driver.find_element_by_xpath('//div[@class="org-top-card-summary-info-list__info-item"][2]').text
	print(followers)
	location_followers=driver.find_element_by_xpath('//div[@class="inline-block"]').text
	print(location_followers)
	website=driver.find_element_by_xpath('//*[@id="ember58"]').get_attribute('href')
	print(website)
	about=f"{driver.current_url}about"
	driver.get(about)
	time.sleep(2)
	about=driver.find_element_by_xpath('//section/p').text
	print(about)
	abouts=driver.find_elements_by_xpath('//dl[@class="overflow-hidden"]/dd')
	for details in abouts:
		details=details.text
		print(details)
		"""
		index0.append()
		index0.append()
		index0.append()
		index0.append()
		index0.append()
		index0.append()
		index0.append()
		index0.append()
		index0.append()
		index0.append()
		index0.append()
		index0.append()
		index0.append()
		"""
#driver.quit()
