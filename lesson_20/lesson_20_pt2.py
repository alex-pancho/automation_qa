import time
from datetime import datetime
from datetime import timedelta

mydatetime = datetime.fromtimestamp(1706551390)
print(mydatetime)
print(type(mydatetime))

nix_time_now = mydatetime.strftime("%H:%M:%S and %Y-%m-%d")
print(nix_time_now)


incoming_date = "Aug 24, 1991"
dt_incoming_date = datetime.strptime(incoming_date, '%b %d, %Y')

print(dt_incoming_date+timedelta(hours=16, minutes=25))
print("*"*88)
d = datetime.today()
print(d)
print(d.isocalendar())
print(d.isoformat())
print(d.isoweekday())
print(d.timetuple())
print(d.weekday())
time_from_day_x = d - dt_incoming_date
print(time_from_day_x)
# thre hours diff
thd = d + timedelta(hours=3, minutes=5, seconds=23)
print(thd)

if thd - d >= timedelta(hours=3):
    print("ok")
else:
    print("err")
