from datetime import timedelta
delta = timedelta(days=50, seconds=25, microseconds=10, milliseconds=29000, minutes=12, hours=8, weeks=2)

print(delta)

from datetime import date
try:
    data = date(year=2023, month=3, day=27)
    next_date = data.strftime("%A %d, %B %Y")
    print(next_date[6:16])
except ValueError:
    print("Invalid date")

from datetime import datetime

current_date = datetime.now()
print(f"Current date and time is: {current_date}")

