# Task #3
# - requests (external library that can be installed using pip)
# - how to make a GET / POST / DELETE / PUT / PATCH request using python.
# - how to give custom HTTP / HTTPS headers to a request made by python.
# - how to give data to GET request as query.
# - how to give data to POST request as json.
# - how to handle the data returned from requests and how to convert it into json.
# - how to check if request sent was failed or successful or redirected.

import requests
import json

#==================================================================================================
# - How to make Get request using python
#==================================================================================================

# response = requests.get('https://github.com/timeline.json')
# print(type(response.text))
# json_data = response.json()
# print(json_data)

# print("\n#- Header.")
# print (response.headers['status'])
# print("\n#- Text.")
# # print (response.text)
# print (json_data['message'])


#==================================================================================================
# - How to make Post request using python
#==================================================================================================

# Example 1

# # defining the api-endpoint 
# API_ENDPOINT = "http://pastebin.com/api/api_post.php"
 
# # your API key here
# API_KEY = "871451d6b0da634db78e114255a4023b"
 
# # your source code here
# source_code ={"hello world"}
# data = {'api_dev_key':API_KEY,
#         'api_option':'paste',
#         'api_paste_code':source_code,
#         'api_paste_format':'python'}
 
# # sending post request and saving response as response object
# response = requests.post(url = API_ENDPOINT, data = data)
 
# # extracting response text 
# pastebin_url = response.text
# print("The pastebin URL is:%s"%pastebin_url)
# # response= requests.get(pastebin_url)
# # pastebin_url = response.text
# # print("The pastebin URL is:%s"%pastebin_url)

# Example 2

# data= {'name': 'nazim', 'age': '20'}

# response = requests.post("http://httpbin.org/post", data=data)
# json_data = response.json()
# print(json_data['form']['name'])




#==================================================================================================
# how to give custom HTTP / HTTPS headers to a request made by python.
#==================================================================================================

#  Using Post Method

# url = 'http://httpbin.org/post'
# data = {'name': 'nazim', 'age': '20'}
# headers = {'User-Agent': 'my-app/0.0.1'}
# response= requests.post(url,headers=headers,data=data)
# json_data = response.json()
# print(json_data)

#  Using Get Method

# headers = {'User-Agent': 'my-app/0.0.1'}
# response= requests.get('http://httpbin.org/get',headers=headers)
# json_data = response.json()
# print (json_data)

#==================================================================================================
# - how to give data to POST request as json.
#==================================================================================================

# data= {'name': 'nazim', 'age': '20'}
# response= requests.post("http://httpbin.org/post", data=data)
# json_data = response.json()
# print(json_data['form']['name'])

#==================================================================================================
# -  how to handle the data returned from requests and how to convert it into json.
#==================================================================================================

# response= requests.get('https://github.com/timeline.json')
# print(type(response.text))
# json_data = response.json()
# print(json_data)

# print("\n#- Header.")
# print (response.headers['status'])
# print("\n#- Text.")
# # print (response.text)
# print (json_data['message'])


#==================================================================================================
# - how to check if request sent was failed or successful or redirected.
#==================================================================================================


# url = 'http://httpbin.org/status/404'
# response= requests.post(url)
# if (response.status_code==200):
# 	print("Request is successfuly sent")
# elif (response.status_code==404):
# 	print("Request Failed")
# elif (response.status_code==405):
# 	print("Function error")
# elif (response.status_code==300):
# 	print("Request redirected")

