import requests
from lxml import etree
from bs4 import BeautifulSoup

url = "https://www.whatmobile.com.pk/"

response  = requests.get(url)

data = response.text

soup = BeautifulSoup(data,"html.parser")

# ================================================================================================
#  Get all `<a>` anchor tags and their respective links. (only unique links).
# ================================================================================================

# for anchor_tag in soup.find_all('a'):
# 	print("%s :%s"%(anchor_tag.get("title"),anchor_tag.get("href")))

# ================================================================================================
#  Get all `<img>` image tags and their respective source links. (only unique links).
# ================================================================================================

# for img_tag in soup.find_all('img'):
	# print(img_tag.get('src'))

# ================================================================================================
#  Get all the name and price of mobile 
# ================================================================================================

	
# mobile_name = list()
# for name in soup.find_all("a", class_="BiggerText"):
#  	mobile_name.append(name.get("title"))


# mobile_price = list()
# for price in soup.find_all("span", class_="PriceFont"):
#  	mobile_price.append(price.text)

# mobile_info= dict()
# for data in range(len(mobile_name)):
# 	mobile_info[mobile_name[data]] = mobile_price[data]

# for name,price in mobile_info.items():
# 	print("Name :%s \nPrice :%s"%(name,price))

# ================================================================================================
#  How to parse xml data using  lxml library 
# ================================================================================================


 
# def parse_Book_Xml_All(xmlFile):
 
# 	context = etree.iterparse(xmlFile)
# 	book_dict = {}
# 	books = []
# 	for action,element in context:
# 		if not element.text:
# 			text = "None"
# 		else:
# 			text = element.text
# 	# print (element.tag + " => " + text)
# 		book_dict[element.tag] = text
# 		if element.tag == "book":
# 			books.append(book_dict)
# 			book_dict = {}
# 	return books
 
# if __name__ == "__main__":
#    book = parse_Book_Xml_All("sample.xml")
#    print(book[2])

# ================================================================================================
#  How to parse specific xml data using  lxml library 
# ================================================================================================


# def parse_Book_Xml_Specific(xmlFile):

# 	context = etree.iterparse(xmlFile)
#     book_dict = dict()
#     books = list()
#     for action,element in context:
#         if element.tag == "title":
# 	        book_dict[element.tag] = element.text
#         if element.tag == "book":
#             books.append(book_dict)
#             book_dict = {}
#     return books
 
# if __name__ == "__main__":
#    book_title = parse_Book_Xml_Specific("sample.xml")
   
#    for title in range(len(book_title)):
#    	print(book[title])






