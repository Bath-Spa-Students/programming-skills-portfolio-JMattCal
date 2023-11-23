#write a python program to display the current data and time
import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the current date and time as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Print the formatted date and time
print("Current Date and Time: " + formatted_datetime)
