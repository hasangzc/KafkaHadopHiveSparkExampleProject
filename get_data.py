import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from parsel import Selector
from webdriver_manager.firefox import GeckoDriverManager



def get_page(url):
	driver = None
	try:
		service = Service(ChromeDriverManager().install())
	
		options = webdriver.ChromeOptions()
		options.headless = True
		options.add_argument("--lang=en")
		options.add_argument("--no-sandbox")
		options.add_argument("--disable-dev-shm-usage")
	
		driver = webdriver.Chrome(service=service, options=options)
		driver.get(url)
	
		WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
	
		selector = Selector(driver.page_source)
		driver.quit()

	except:
		options = webdriver.FirefoxOptions()
		options.headless = True
		options.add_argument("--lang=en")
		options.add_argument("--no-sandbox")
		options.add_argument("--disable-dev-shm-usage")
		
		# driver = webdriver.Firefox(executable_path=GeckoDriverManager(cache_valid_range=1).install())
		driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
		driver.get(url)
		# https://github.com/mozilla/geckodriver/releases
		WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
	
		selector = Selector(driver.page_source)
		driver.quit()
	return selector


	



def scrape_daily_search(selector):	
	daily_search_trends = {}

	for date in selector.css('.feed-list-wrapper'):
		date_published = date.css('.content-header-title::text').get()
		daily_search_trends[date_published] = []
		
		for item in date.css('.feed-item-header'):
			index = item.css('.index::text').get().strip()
			title = item.css('.title span a::text').get().strip()
			subtitle = item.css('.summary-text a::text').get()
			source = item.css('.source-and-time span::text').get().strip()
			time_published = item.css('.source-and-time span+ span::text').get().strip()
			searches = item.css('.subtitles-overlap div::text').get().strip()
				
			daily_search_trends[date_published].append({
				'index': index,
				'title': title,
				'subtitle': subtitle,
				'source': source,
				'time_published': time_published,
				'searches': searches,
			})
	
	return json.dumps(daily_search_trends, indent=2, ensure_ascii=False)
	
	


