import datetime


def saturdays(year):
    saturday = 0
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                date = datetime.date(year, month, day)
                if date.weekday() == 5:
                    saturday += 1
            except ValueError:
                pass
    return saturday


print(saturdays(2022))
