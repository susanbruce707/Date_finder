##<-Datetime and Timedelta use and simple demonstation
import datetime
from datetime import date
from datetime import timedelta
affirmations = ("You are:",
                "Acceptable",
                "Forgiveable",
                "Lovable",
                "Capable",
                "Competent",
                "In Christ Jesus",
                "*******")
for item in affirmations:
    print(item)
year = 2018
month = 1
day = 10
start_date = datetime.date(year, month, day)
week = start_date + timedelta(7)
fortnight = start_date + timedelta(14)
threeweek = start_date + timedelta(21)
fourweek = start_date + timedelta(28)
fiveweek = start_date + timedelta(35)
sixweek = start_date + timedelta(42)
print("start date date is", start_date,
      "\nplus 1 week is", week,
      "plus 5 weeks is", fiveweek)
print()
datetimeFormat = '%Y-%m-%d%f'
date1 = '2018-01-10'
date2 = '2018-04-16'
print("first date is", date1)
print()
print("second date is", date2)
print()
diff = datetime.datetime.strptime(date2, datetimeFormat)\
       - datetime.datetime.strptime(date1, datetimeFormat)
days_diff = diff.days
weeks_diff = days_diff // 7
weeks_and_days_diff = (weeks_diff, (days_diff - (weeks_diff * 7)))
print("between", date1, "and", date2, "is", diff.days, "days")
print()
print("this is ",
      str(weeks_diff),
      " Weeks and ",
      str(weeks_and_days_diff[1]),
      " Days")
print()

period = 14
periods = days_diff // period
print("number of two week periods is", periods)
print()
print("the date from ", date1, "every 2 weeks is")
for delta in range(period, (periods*period+1), period):
    print(start_date + timedelta(delta))

