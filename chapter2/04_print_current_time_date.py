#  Program that displays the current date and time
import datetime

now = datetime.datetime.now()

selected_date = (12,2,22)

print("Current date and time is :" , now)
print(now.strftime("%Y/%m/%d %H:%M:%S"))

print("The examination will start from: %i/ %i/ %i" % selected_date)