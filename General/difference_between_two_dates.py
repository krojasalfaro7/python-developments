from datetime import datetime


def difference_between_dates(start_date: str, end_date: str):

    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

    return (end_date >= start_date)


print(difference_between_dates("2021-10-22", "2021-10-23"))
