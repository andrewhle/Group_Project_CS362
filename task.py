def conv_num(num_str):
    """Takes a string and converts it to a base 10 number then
    returns it. Can handle strings representing integer, float,
    and hexadecimal string representations of numbers.
    """
    return 0


def my_datetime(num_sec):
    """Takes an integer value that represents the number of seconds
    since the epoch, January 1st 1970, and returns that date as a
    string in the format MM-DD-YYY.
    """
    days_in_months = {
        "01": 31,
        "02": 28,
        "03": 31,
        "04": 30,
        "05": 31,
        "06": 30,
        "07": 31,
        "08": 31,
        "09": 30,
        "10": 31,
        "11": 30,
        "12": 31
    }
    seconds_in_day = 86400
    days = num_sec // seconds_in_day
    year, day_count = calc_year_and_days(days)
    day = 0
    for month in days_in_months:
        if day_count == 0:
            return month + "-" + str(day) + "-" + str(year)
        while day < days_in_months[month]:
            if day_count == 0:
                day_str = str(day)
                if len(day_str) == 1:
                    day_str = "0" + day_str
                return month + "-" + day_str + "-" + str(year)
            day += 1
            day_count -= 1
        day = 0


def calc_year_and_days(days):
    """Takes a number of days and returns the year since the epoch
    and the amount of days until the exact date.
    """
    year = 1970
    day_count = 1
    for _ in range(days):
        day_count += 1
        if day_count == 366:
            year += 1
            day_count = 0
        if day_count == 365:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 != 0:
                        year += 1
                        day_count = 0
            else:
                year += 1
                day_count = 0
    return (year, day_count)


def conv_endian(num, endian='big'):
    """Takes an integer value 'num' and converts it to a hexamdecimal
    number. Endian type is determined by the flag 'endian'. Number is
    converted and returned as a string.
    """
    return "00"
