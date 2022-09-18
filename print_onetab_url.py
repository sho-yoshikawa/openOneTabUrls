from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import sys

# GREEN = "\033[32m"
# BLUE = "\033[34m"
# PURPLE = "\033[35m"
# ENDC = "\033[0m"

# def printTitle(title):
# 	print(GREEN, title, ENDC)

# def printUrl(url):
# 	print(BLUE, url, ENDC)


options = webdriver.ChromeOptions()
options.add_argument("--headless")
b = webdriver.Chrome(ChromeDriverManager().install(),options=options)


def printUrls(urls):
	for url in urls:
		print(url[1])


if len(sys.argv) > 1:
	url = sys.argv[1]
else:
	print("no arguments")
b.get(url)
tabContainers = b.find_elements(By.CLASS_NAME, "tabGroupContainer")

urls = []
for tabContainer in tabContainers:
	aTag = tabContainer.find_element(By.TAG_NAME, "a")
	title = aTag.text
	url = aTag.get_attribute("href")
	urls.append([title, url])

printUrls(urls)
