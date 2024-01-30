import datetime
import pytz

def datetime_to_iso_8601_format(datetime_string, timezone):
    datetime_obj = datetime.datetime.strptime(datetime_string, "%Y-%m-%dT%H:%M:%S.%f")
    datetime_obj = datetime_obj.astimezone(timezone)
    return datetime_obj.isoformat(timespec='milliseconds')



datetime_string = "2023-10-30T16:47:23.605665"
timezone = pytz.timezone("America/Mexico_City")

datetime_converted = datetime_to_iso_8601_format(datetime_string, timezone)

print(type(datetime_converted))
print(datetime_converted)