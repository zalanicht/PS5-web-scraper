from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from threading import Thread
import time

def bestbuydisc():
	options = Options()
	options.add_argument('--headless')
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	driver = webdriver.Chrome(options = options)
	driver.set_page_load_timeout(30)
	driver.get('https://www.bestbuy.ca/en-ca/product/playstation-5-console-online-only/14962185')

	all_page = driver.page_source
	#all_span = driver.find_elements_by_tag_name("span")
	#all_span = [i.text for i in all_span]

	if "Coming soon" in all_page:
		print("\tbestbuydisc".ljust(20," "),"not in stock")
	else:
		print("BESTBUYDISC ITEM IS IN STOCK!!!!!!!!!!!!!!!!!!!!!!!")

	driver.close()

def bestbuydigital():
	options = Options()
	options.add_argument('--headless')
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	driver = webdriver.Chrome(options = options)
	driver.set_page_load_timeout(30)
	driver.get('https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-console-online-only/14962184')

	all_page = driver.page_source
	#all_span = driver.find_elements_by_tag_name("span")
	#all_span = [i.text for i in all_span]

	if "Coming soon" in all_page:
		print("\tbestbuydigital".ljust(20," "),"not in stock")
	else:
		print("BESTBUYDIGITAL ITEM IS IN STOCK!!!!!!!!!!!!!!!!!!!!!!!!!")

	driver.close()

def ebgamesdisc():
	options = Options()
	options.add_argument('--headless')
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	driver = webdriver.Chrome(options = options)
	driver.set_page_load_timeout(30)
	driver.get('https://www.ebgames.ca/PS5/Games/877522/playstation-5')
	
	all_page = driver.page_source
	
	if "Out of Stock" in all_page:
		print("\tebgamesdisc".ljust(20," "),"not in stock")
	else:
		print("EBGAMESDISC ITEM IS IN STOCK!!!!!!!!!!!!!!!!!!!!!!!!!")
	
	driver.close()

def ebgamesdigital():
	options = Options()
	options.add_argument('--headless')
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	driver = webdriver.Chrome(options = options)
	driver.set_page_load_timeout(30)
	driver.get('https://www.ebgames.ca/PS5/Games/877523/playstation-5-digital-edition')
	
	all_page = driver.page_source
	
	if "Out of Stock" in all_page:
		print("\tebgamesdigital".ljust(20," "),"not in stock")
	else:
		print("EBGAMESDIGITAL ITEM IS IN STOCK!!!!!!!!!!!!!!!!!!!!!!!!!")
	
	driver.close()

def thesource():
	options = Options()
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	driver = webdriver.Chrome(options = options)
	driver.set_page_load_timeout(30)
	driver.get('https://www.thesource.ca/en-ca/ps5')
	
	all_page = driver.page_source
	
	if "Due to exceptional demand, we are currently out of stock of PS5." in all_page:
		print("\tthe source".ljust(20," "),"not in stock")
	else:
		print("THE SOURCE ITEM IS IN STOCK!!!!!!!!!!!!!!!!!!!!!!!!!")
	
	driver.close()

def walmart():
	options = Options()
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	driver = webdriver.Chrome(options = options)
	driver.set_page_load_timeout(30)
	driver.get('https://www.walmart.ca/en/ps5-xbox-xs-out-of-stock')
	
	all_page = driver.page_source
	
	if "out of stock" in all_page:
		print("\twalmart".ljust(20," "),"not in stock")
	else:
		print("WALMART ITEM IS IN STOCK!!!!!!!!!!!!!!!!!!!!!!!!!")
	
	driver.close()

def toysrus():
	options = Options()
	options.add_argument('--headless')
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	driver = webdriver.Chrome(options = options)
	driver.set_page_load_timeout(30)
	driver.get('https://www.toysrus.ca/en/toysrus/Category/Video-Games/PlayStation/PlayStation-5')

	all_page = driver.page_source

	if 'https://www.toysrus.ca/on/demandware.static/-/Library-Sites-toys-global/default/dw4bd5d542/images/pages/TRU-d-cate-ban-PS5-Nov12-e.jpg' in all_page:
		print("\ttoysrus".ljust(20," "),"not in stock")
	else:
		print("TOYSRUS ITEM IS IN STOCK!!!!!!!!!!!!!!!!!!!!!!!!!")

	driver.close()

threads = []

threads.append(Thread(target = bestbuydisc))
threads.append(Thread(target = bestbuydigital))
threads.append(Thread(target = ebgamesdisc))
threads.append(Thread(target = ebgamesdigital))
threads.append(Thread(target = thesource))
threads.append(Thread(target = walmart))
threads.append(Thread(target = toysrus))

for x in threads:
	x.start()
for x in threads:
	x.join()

input('\n\tPress ENTER to exit')