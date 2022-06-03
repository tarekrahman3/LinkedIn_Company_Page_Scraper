# -*- coding: utf-8 -*-
#author: Tarek R.
#date: Oct 12, 2021

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

out=[]
urls = pd.read_csv('import.csv').links.tolist()
driver = webdriver.Chrome(service=Service("/home/tarek/Downloads/chromedriver"))
time.sleep(2)
driver.get('https://www.linkedin.com/login')
while True:
	if "feed" in driver.current_url:
		break

class COMPANY_PAGE():
	def title():
		try:
			return driver.find_element(By.XPATH, '//h1/span').text
		except:
			return None

	def about():
		try:
			return driver.find_element(By.XPATH, '//p[contains(@class,"break-words white")]').text
		except:
			return None

	def website():
		try:
			return driver.find_element(By.XPATH, '//div[@class="org-top-card-primary-actions__inner"]//a').get_attribute("href")
		except:
			return None
	def employeesLink():
		try:
			return driver.find_element(By.XPATH,'//*[contains(@href,"/search/results/people/?currentCompany=")]').get_attribute('href')
		except:
			return None
	def industry():
		try:
			return driver.find_element(By.XPATH, '//*[text()="Industry"]/following-sibling::*').text
		except:
			return None
	def totalEmployees():
		try:
			return driver.find_element(By.XPATH, '//*[contains(@href,"results/people/")]/span').text
		except:
			return None



for index, url in enumerate(urls):
	driver.get(url + '/about')
	time.sleep(3)
	out.append({
		'source':url,
		'title':COMPANY_PAGE.title(),
		'industry':COMPANY_PAGE.industry(),
		'website':COMPANY_PAGE.website(),
		'totalEmployees':COMPANY_PAGE.totalEmployees(),
		'employeesLink':COMPANY_PAGE.employeesLink(),
		'about':COMPANY_PAGE.about()
		})
	print(f"{index} | {out[-1]['title']} | {out[-1]['website']} | {out[-1]['employeesLink']} | {out[-1]['industry']} | {out[-1]['totalEmployees']}")

pd.DataFrame(out).to_csv('export.csv', index=False)
