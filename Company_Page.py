# -*- coding: utf-8 -*-
#author: Tarek R.
#date: Oct 12, 2021

import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
import pandas as pd
import time

out=[]
urls = pd.read_csv('import.csv').links.tolist()
driver = uc.Chrome()
time.sleep(2)
driver.get('https://www.linkedin.com/login')
while True:
	if "https://www.linkedin.com/login" in driver.current_url:
		time.sleep(2)
	else:
		break

class COMPANY_PAGE():
	def title():
		return driver.find_element(By.XPATH, '//h1/span').text

	def about():
		try:
			return driver.find_element(By.XPATH, '//p[contains(@class,"break-words white")]').text
		except:
			return None

	def website():
		try:
			return driver.find_element(By.XPATH, '//section[contains(@class, "artdeco-card p4 mb3")]//a[contains(@href, "http")]').get_attribute("href")
		except:
			return None


for index, url in enumerate(urls):
	driver.get("https://" + url + '/about')
	time.sleep(3)
	out.append({
		'source':url,
		'title':COMPANY_PAGE.title(),
		'website':COMPANY_PAGE.website(),
		'about':COMPANY_PAGE.about()
		})
	print(f"{index} | {out[-1]['title']} | {out[-1]['website']}")

pd.DataFrame(out).to_csv('export.csv', index=False)
