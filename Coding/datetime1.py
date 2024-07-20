import datetime as dt

now=dt.datetime.now() 
print(now) 
year=now.year
month=now.month
day1=now.weekday()
print(day1)

DOB=dt.datetime(year=2005, month=9, day=24, hour=9, minute=30)
print(DOB)