import datetime
import pytz

TIMEZONE = "America/Mexico_City"

date_time_str = '2022-12-31 00:00:00.000000'
dtime = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
#dtime = datetime.datetime.now()

timezone = pytz.timezone(TIMEZONE)
dtzone = timezone.localize(dtime)

print("Time Zone: ", dtzone.tzinfo)
print("Datetime: ", dtzone)

tstamp = dtzone.timestamp()
print("Integer timestamp: ", int(round(tstamp)))
