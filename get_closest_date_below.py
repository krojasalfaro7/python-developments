import datetime

def get_closest_date_below(listdate, date):
    """
        Se obtiene una lista de fechas en string y se devuelve
        la fecha igual o mas cercana por debajo a la fecha dada

    :param listdate: lista de fechas en string y en formato %Y-%m-%d
    :param date: fecha en string y en formato %Y-%m-%d
    :return:
    """
    dateint = tuple(map(lambda x: int(x), date.split("-")))
    datedatetime = datetime.date(dateint[0], dateint[1], dateint[2])
    listdateformat = list(map(lambda x: tuple(x.split('-')), listdate))
    listdatedatetime = list(map(lambda x: datetime.date(int(x[0]), int(x[1]), int(x[2])), listdateformat))
    listdatedatetimeprocess = list(map(lambda x: (datedatetime - x).days, listdatedatetime))
    datelist = list(filter(lambda x: x[1] >= 0, list(enumerate(listdatedatetimeprocess))))

    return listdate[min(datelist, key=lambda t: t[1])[0]]


lista = ['2018-06-24', '2019-06-24', '2020-06-30', '2020-06-12', '2020-06-2', '2020-06-1']
print(get_closest_date_below(lista, "2019-06-12"))
