#  Program that displays the current date and time
import datetime

now = datetime.datetime.now()

print("Current date and time is :" , now)

print(now.strftime("%Y/%m/%d %H:%M:%S"))