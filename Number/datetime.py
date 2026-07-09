from datetime import datetime

now = datetime.now()

full_date_time = now.strftime(
    "%Y-%m-%d %H:%M:%S"
)  # Full date and time ie. 2010/03/02 12:01:22
date_only = now.strftime("%Y-%m-%d")  # Date only ie. 2010/03/02
time_only_24hr = now.strftime("%H:%M:%S")  # Time in 24-hour format
time_only_12hr = now.strftime("%I:%M:%S %p")  # Time in 12-hour format with AM/PM
day_of_week = now.strftime("%A")  # Day of the week ie. Friday
month_name = now.strftime("%B")  # Full month name ie. June

print("Full Date and Time:", full_date_time)
print("Date Only:", date_only)
print("Time (24-hour format):", time_only_24hr)
print("Time (12-hour format):", time_only_12hr)
print("Day of the Week:", day_of_week)
print("Month Name:", month_name)
