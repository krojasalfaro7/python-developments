import datetime
import pytz
from datetime import timedelta


def generate_range_dates(days: int) -> list:

    timezone = pytz.timezone("America/Mexico_City")
    current_date = datetime.datetime.now()
    start_date = current_date.astimezone(timezone).date()
    for day in range(days+1):
        yield str(start_date + timedelta(days=day))


range_dates = list(generate_range_dates(days=7))

print(range_dates)
print("2021-11-10" in range_dates)
