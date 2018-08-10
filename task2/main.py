# Task #3
# - json (builtin library)
# - how to read / write json content to a file.
# - how to convert a string content to json and a json content to string.
# - how to sort json content.
import json

#==================================================================================================
# - How to write in Json format in a file
#==================================================================================================

# data = {}  
# data['Employee'] = []  
# data['Employee'].append({  
#     'name': 'Nazim',
#     'gmail': 'nazim.com',
#     'city': 'Gujrat',
#     'age': '20'
# })
# data['Employee'].append({
#     'name':'Arij',
#     'gmail':'arij.com',
#     'city':'lahore',
#     'age': '19'

#     })
# data['Manager'] = []  
# data['Manager'].append({  
#     'name': 'Fasial Sharif',
#     'gmail': 'Fasial.com',
#     'city': 'lahore'
# })
# data['Manager'].append({  
#     'name': 'Ali Raza',
#     'gmail': 'Ali.com',
#     'city': 'lahore'
# })
# with open('data.txt', 'w') as outfile:  
#     json.dump(data, outfile, indent=4)

#==================================================================================================
# - How to read in Json format from a file
#==================================================================================================

# with open('data.txt') as json_file:
#     data=json.load(json_file)
#     print("Employee:\n")
#     for people in data['Employee']:
#         print('Name: ' + people['name'])
#         print('gmail: ' + people['gmail'])
#         print('city: ' + people['city'])
#         print('')
#     print("Manager:\n")
#     for people in data['Manager']:
#         print('Name: ' + people['name'])
#         print('gmail: ' + people['gmail'])
#         print('city: ' + people['city'])
#         print('')

#==================================================================================================
# - How to convert a string content to json.
#==================================================================================================

# string = '{"success": "true", "status": 200, "message": "Hello"}'
# json_obj = json.loads(string)
# print (type(json_obj),json_obj["success"], json_obj["status"])

#==================================================================================================
# - How to convert a json content to string. 
#==================================================================================================

# data = {'Name': None}
# data=json.dumps(data)
# print(type(data))

#==================================================================================================
# - How to sort json content .
#==================================================================================================

# def sort_by_age(age):
#     '''
#     helper function for sorting a list of dictionaries'''
#     return age.get('age', None)
# with open('data.txt') as json_file:
#     data=json.load(json_file)
#     for row in sorted(data['Employee'], key=sort_by_age):
#             print('Name: ' + row['name'])
#             print('gmail: ' + row['gmail'])
#             print('city: ' + row['city'])
#             print('Age: ' + row['age'])
#             print('')
