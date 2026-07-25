from datetime import datetime, timezone

now = datetime.now(timezone.utc)

full_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
date_only = now.strftime("%Y-%m-%d")
time_only_24hr = now.strftime("%H:%M:%S")
time_only_12hr = now.strftime("%I:%M:%S %p")
day_of_week = now.strftime("%A")
month_name = now.strftime("%B")

print("Full Date and Time:", full_date_time)
print("Date Only:", date_only)
print("Time (24-hour format):", time_only_24hr)
print("Time (12-hour format):", time_only_12hr)
print("Day of the Week:", day_of_week)
print("Month Name:", month_name)
