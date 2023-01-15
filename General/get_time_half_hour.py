import datetime

half_hour = datetime.timedelta(minutes=30)


def validate_half_hour_allowed(times, input_time):
    for time in enumerate(times):
        if not input_time >= time[1]:
            try:
                before_time = times[time[0]-1]
                present_time = time[1]
                before_time_more_half_hour = before_time + half_hour
                present_time_less_half_hour = present_time - half_hour
                if (present_time - before_time >= half_hour) and before_time_more_half_hour <= input_time <= present_time_less_half_hour:
                    print("Permitido")
                    break
            except IndexError:
                print("permitido")
                break


times = [datetime.timedelta(seconds=27082),
        datetime.timedelta(seconds=35082),
        datetime.timedelta(seconds=37082),
        datetime.timedelta(seconds=47082),
        datetime.timedelta(seconds=52082),
        datetime.timedelta(seconds=64492)]

input_time = datetime.timedelta(seconds=60192)
# hour, minute, second = tuple(map(lambda x: int(x), '05:37:45'.split(":")))
# input_time_from_string = datetime.timedelta(hours=hour, minutes=minute, seconds=second)

if len(times) > 1:
    validate_half_hour_allowed(times, input_time)
elif len(times) == 1:
    if not (input_time <= (times[0] - half_hour)) or (input_time >= (times[0] + half_hour)):
        print(f"Hora ocupada, intenta con una hora menor a {times[0] - half_hour} or mayor a {times[0] + half_hour}")
