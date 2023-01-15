from datetime import datetime
from networkdays import networkdays


def difference_between_dates_excluding_weekends(start_date: str, end_date: str):

    total_days = networkdays.Networkdays(
        datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S").date(),
        datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S").date()
    )
    return len(total_days.networkdays()) - 1


print(difference_between_dates_excluding_weekends("2021-10-22 15:54:01", "2021-10-25 15:54:01"))
