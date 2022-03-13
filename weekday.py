from datetime import date #import the package to get the date
import calendar  #import the package to get the calendar
today = date.today() #create a variable with today's date
today = calendar.day_name[today.weekday()] #overwrite the today variable with the formula for today's date
#print(calendar.day_name[today.weekday()]) #get today's day
#print (today)
#type(today)

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] #create a list with the weekdays' names
weekend = ["Saturday", "Sunday"] #create a list with the wekkend's names' names (I won't need it)

for day in weekdays: #create a loop for every day in the weekdays
    if today == day: #create a condition satisfied if today's day match the weekdays
        print ("Yes, unfortunately today is a weekday.") #print the output
    else:
        print ("It is the weekend, yay!") 
    break #stop the loop once the condition is satisfied




#reference1 https://www.delftstack.com/howto/python/python-datetime-day-of-week/