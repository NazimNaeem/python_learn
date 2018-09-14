import csv
from selenium import webdriver

MAX_PAGE_NUM = 5
MAX_PAGE_DIG = 3

with open('result.csv','w')as f:
	f.write("Buyers,Prices\n")

driver = webdriver.Firefox()

for i in range(1,MAX_PAGE_NUM + 1):
	page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
	url = "http://econpy.pythonanywhere.com/ex/" + page_num +".html"

	driver.get(url)

	buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
	prices = driver.find_elements_by_class_name('item-price')


	total_item = len(buyers)
	with open('result.csv','a') as f:
		for item in range(total_item):
			f.write(buyers[item].text + "," + prices[item].text + "\n")
driver.quit()