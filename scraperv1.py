from selenium import webdriver
#browser = webdriver.Chrome("path/to/chrome/driver")
profile = webdriver.FirefoxProfile()
browser = webdriver.Firefox(firefox_profile=profile)
browser.get("https://www.akc.org/dog-breeds/")
def scrape():
	retry = 0
	didDisconnect = True
	while didDisconnect and retry <= 5:
		try:
			didDisconnect = scrapeBreeds(browser)
		except:
			print("ERROR... Retrying...")
			retry += 1
def scrapeBreeds(browser):
	breedPagesCount = len(browser.find_elements_by_class_name("breed-letters-filter__letter")) - 1
	page = 0
	didDisconnect = True
	for p in range(breedPagesCount):
		breedPages = browser.find_elements_by_class_name("breed-letters-filter__letter")
		breeds = browser.find_elements_by_xpath('//*[@id="breed-type-card-"]/a/h3')
		for b in breeds:
			temp = b.text
			print(temp)			
		page += 1
		breedPages[page].click()
		didDisconnect = False
	return didDisconnect
scrape()
browser.close()
