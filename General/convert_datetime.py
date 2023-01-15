import datetime
import pytz


def format_utc_to_local_datetime(str_datetime: str, timezone: str) -> str:
    input_datetime = datetime.datetime.strptime(str_datetime, "%Y-%m-%dT%H:%M:%S.%f%z")
    input_datetime.replace(tzinfo=datetime.timezone.utc)
    local_timezone = pytz.timezone(timezone)
    local_datetime = input_datetime.replace(tzinfo=pytz.utc)
    local_datetime = local_datetime.astimezone(local_timezone)
    return local_datetime.strftime("%Y-%m-%d %H:%M:%S")


print(format_utc_to_local_datetime("2021-09-23T20:37:09.731Z", "America/Mexico_City"))
