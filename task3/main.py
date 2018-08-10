# #===================================================================================================================
# 										#Task no 3
# #===================================================================================================================
# # look into 2 python libraries:  - datetime & time
# # - get current date.
# # - get current time.
# # - get complete timestamp (date + time)
# # - get previous sunday from current date (current date means the time whenever the script is run, no hardcoding)
# # - get coming sunday from current date (current date means the time whenever the script is run, no hardcoding)
# # - similarly, write a function that can get you previous and coming CERTAIN day. (certain day can be sunday, monday or any day of the week. it can be changed by the parameter given to function).

# # - add / subtract a certain number of days to current date.
# # - similarly, add / subtract a certain number of hours /  minutes to current date. (very similar to above task)
# # - compare two dates. (each date or time is an object in python, you should know how to compare them like date1 > date2 etc.)

# # - get timestamp in seconds.
# # - convert timestamp in seconds to date object & date object to seconds timestamp.

import datetime,time


# #===================================================================================================================
# # - How get current date.
# #===================================================================================================================

# current_date = datetime.date.today()
# print("Current Date :" + current_date)

# #===================================================================================================================
# # - How get current time.
# #===================================================================================================================

# # Method no: 1

# current_time=datetime.datetime.now().time()
# print ("Current Time :" + current_time.strftime("%I:%M:%S"))

# # Method no: 2

# current_time=time.strftime("%H:%M:%S")
# print ("Current Time :" + current_time)

# #===================================================================================================================
# # - How get complete timestamp (date + time).
# #===================================================================================================================

# current_date_time = datetime.datetime.now()
# print("Current Date :" + str(current_date_time))

# #===================================================================================================================
# # - How get previous sunday from current date .
# #===================================================================================================================

# # Method no 1:

# today = datetime.date.today()			# return currnt date
# index = today.isoweekday()    			# return int Mon=1,Tue=2,.....Sun=7
# sun = today-datetime.timedelta(index)
# print("Previous Sunday is on :" + str(sun))

# Method no 2:

# today = datetime.date.today()			# return currnt date
# index = (today.weekday()+1)    			# return int Mon=0,Tue=1,.....Sun=6
# sun = today-datetime.timedelta(index)
# print("Previous Sunday is on :" + str(sun))

# #===================================================================================================================
# # - How get coming sunday from current date .
# #===================================================================================================================

# today = datetime.date.today()			# return currnt date
# index = (today.isoweekday())    			# return int Mon=1,Tue=2,.....Sun=7
# sun = today +datetime.timedelta(7-index)
# print("Coming Sunday is on :" + str(sun))

# #===================================================================================================================
# # - How get previous any day from current date .
# #===================================================================================================================

# today = datetime.date.today()
# sun = today-datetime.timedelta(today.isoweekday())
# mon=today - datetime.timedelta(days=today.isoweekday()-1)
# tues=today - datetime.timedelta(days=today.isoweekday()-2)
# wed=today - datetime.timedelta(days=today.isoweekday()-3)
# thurs=today - datetime.timedelta(days=today.isoweekday()-4)
# # print(sun)
# # print(mon)
# print(tues)
# print(wed)
# print(thurs)
  
# print(index)
# print(str(datetime.timedelta(days=today.isoweekday() + 2)))
# friday = today - datetime.timedelta(days=today.isoweekday() + 2)
# print(friday)


# #===================================================================================================================
# # - How to add / subtract a certain number of days to current date.
# #===================================================================================================================

# days=input("Enter the number of days :")
# oper=input("Enter the operator +/- :")

# if(oper=='-'):
# 	result = datetime.datetime.today() - datetime.timedelta(days=int(days))
# if (oper=='+'):
# 	result = datetime.datetime.today() + datetime.timedelta(days=int(days))
# print(result)

# #===================================================================================================================
# # - How to add / subtract a certain number of hours /  minutes to current date.
# #===================================================================================================================

# hours=input("Enter the number of hours :")
# minutes=input("Enter the number of minutes :")
# oper=input("Enter the operator +/- :")
# if(oper=='-'):
# 	result = datetime.datetime.today() - datetime.timedelta(hours=int(hours), minutes=int(minutes))
# if(oper=='+'):
# 	result = datetime.datetime.today() + datetime.timedelta(hours=int(hours), minutes=int(minutes))

# print(result.strftime('%H:%M %p'))

# #===================================================================================================================
# # - How to  compare two dates.
# #===================================================================================================================

# date=input("Enter the date in format YYYY-MM-DD :")
# date= datetime.datetime.strptime(date, '%Y-%m-%d')
# today_date = datetime.datetime.today()
# if(date > today_date):
# 	print("Your enter date is greater than today date")
# elif(date < today_date):
# 	print("Your enter date is less than today date")
# else:
# 	print("Your date is equal to today date")

# #===================================================================================================================
# # - How to get timestamp in second.
# #===================================================================================================================

# timestamp_in_second = datetime.datetime.now().timestamp()
# print("Timestamp in second :" + str(timestamp_in_second))

# #===================================================================================================================
# # - How to get convert timestamp in seconds to date object & date object to seconds timestamp..
# #===================================================================================================================

# timestamp_in_second = datetime.datetime.now().timestamp()
# print("Timestamp in second :" + str(timestamp_in_second))

# date_object=datetime.datetime.fromtimestamp(timestamp_in_second)
# print("Date_object :" + str(date_object))

# #===================================================================================================================
# # - How to sleep (wait) for certain number of seconds / minutes.
# #===================================================================================================================

# num = input('How long to wait: ')
# check = input('In seconds or minutes  s/m: ')
# num = float(num)

# if not(check=="m" or check =="s"):
# 	print("Enter s for second or m for minutes")
	
# elif(check=="m"):
# 	num=num*60
# print('Before: %s' % time.ctime())
# time.sleep(num)
# print('After: %s\n' % time.ctime())

# #===================================================================================================================
# # - How to remain on sleep till certain time..
# #===================================================================================================================
# today_date = datetime.datetime.today()
# result=today_date.strftime('%Y-%m-%d ')
# date= datetime.datetime.strptime(result + "12-08", '%Y-%m-%d %H-%M')
# sleep_time=date-today_date

# print('Before: %s' % time.ctime())
# time.sleep(sleep_time.total_seconds())
# print('After: %s\n' % time.ctime())