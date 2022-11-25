def conv_num(num_str):
    """Takes a string and converts it to a base 10 number then
    returns it. Can handle strings representing integer, float,
    and hexadecimal string representations of numbers.
    """
    if not num_str:
        return None
    nums = "1234567890"
    negative = 1
    res = 0
    # Check for valid integer
    if '.' not in num_str and 'x' not in num_str:
        for i in range(len(num_str)):
            if i == 0 and num_str[i] == '-':
                negative = -1
                continue
            if num_str[i] in nums:
                res = res * 10 + (ord(num_str[i]) - 48)
            else:
                return None
        return res * negative
    else:
        return None


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
    decimal_to_hex = {
      0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
      10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
    }
    # create a list of all hex digits. Use to convert to big or little endian
    quotients = []
    abs_num = abs(num)

    while abs_num > 15:
        quotients.append(decimal_to_hex[abs_num % 16])
        abs_num = abs_num // 16
    quotients.append(decimal_to_hex[abs_num])
    if len(quotients) % 2 != 0:
        quotients.append("0")

    # convert strings to bits and combine bits based on endian
    hex_num = ""
    while len(quotients) > 0:
        first = quotients.pop(0)
        second = quotients.pop(0)
        if endian == "big":
            hex_num = second + first + " " + hex_num
        elif endian == "little":
            hex_num += second + first + " "
        else:
            return None

    # return all except last digit which will always be a space based on sign.
    if num >= 0:
        return hex_num[:-1]
    else:
        return "-" + hex_num[:-1]
