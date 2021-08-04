from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
import pandas as pd
import time
import csv
import os
import random

time_array = [5,4,2,10,3]

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--start-maximized")
options.add_argument('--ignore-certificate-errors')
options.add_argument("user-agent=DN")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('user-data-dir=HeraParvin')


driver = webdriver.Chrome(options=options, executable_path='chromedriver')
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
print(driver.execute_script("return navigator.userAgent;"))

driver.get('http://linkedin.com')
input('::')
stealth(
    driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
    )
col0_5=[]
col0=[]
col1=[]
col2=[]
col3=[]
col4=[]
col5=[]
df = pd.read_csv('import.csv', header=0)
links = df.links.to_list()

for i in links:
	col0.append(i)
	driver.get(i+'/about')
	time.sleep(time_array[random.randrange(len(time_array))])
	try:
		title=driver.find_element_by_xpath('//h1/span').text
	except:
		title=''

	try:	
		about = driver.find_element_by_xpath('//p[contains(@class,"break-words white")]').text
	except:
		about = ''
	try:	
		website = driver.find_element_by_xpath('//section[contains(@class, "artdeco-card p4 mb3")]//a[contains(@href, "http")]').get_attribute("href")
	except:
		website = ''
	try:	
		employees = driver.find_element_by_xpath('//a[contains(@href, "results/people")]/span').text
	except:
		employees = ''
	try:	
		followers = driver.find_element_by_xpath('//div[contains(@class, "inline-block")]/div[2]').text
	except:
		followers = ''
	try:	
		ind_loc_fol = driver.find_elements_by_xpath('//div[contains(@class, "org-top-card-summary")]')
		li = []
		for a in ind_loc_fol:
			item = a.text
			li.append(item)
		ind_loc_fol = li
	except:
		ind_loc_fol = ''
	print(f"{links.index(i)}|{title} | {website}|{employees}|{followers}|{ind_loc_fol}")
	col0_5.append(title)
	col1.append(about)
	col2.append(website)
	col3.append(employees)
	col4.append(followers)
	col5.append(ind_loc_fol)
	#time.sleep(time_array[random.randrange(len(time_array))])
driver.quit()
data = {'source': col0,
'title':col0_5,
'about': col1,
'website':col2,
'employees': col3,
'followers': col4,
'ind_loc_fol':col5
}
df = pd.DataFrame(data).to_csv(f'export at {time.ctime()}.csv', index=None, header=True)
