def conv_hex_helper(num_str):
    hex = [
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        'A',
        'B',
        'C',
        'D',
        'E',
        'F'
    ]

    for i in num_str:
        if i not in hex:
            return None

    def get_digit(digit):
        if digit in hex:
            return hex.index(digit)

    dec_num = 0
    power = 0
    for digit in range(len(num_str), 0, -1):
        dec_num = dec_num + ((16 ** power) * get_digit(num_str[digit - 1]))
        power += 1
    return dec_num


def conv_float_helper(num_str):
    int_value = 0
    fraction_value = 0
    sign = 1

    value = {'0': 0,
             '1': 1,
             '2': 2,
             '3': 3,
             '4': 4,
             '5': 5,
             '6': 6,
             '7': 7,
             '8': 8,
             '9': 9}
    decimal = False
    fraction_counter = 1

    for digit in num_str:
        if digit == '-':
            sign = -1
            continue
        if digit == '.':
            decimal = True
            continue
        if decimal:
            fraction_value = (fraction_value * 10) + value[digit]
            fraction_counter *= 10
        else:
            int_value = int_value * 10 + value[digit]

    if decimal:
        int_value = int_value + (fraction_value / fraction_counter)

    return int_value * sign


def conv_num(num_str):
    """Takes a string and converts it to a base 10 number, then
    returns it. Can handle strings representing integer, float,
    and hexadecimal string representations of numbers.
    """

    # Check if valid type
    if not num_str or not isinstance(num_str, str):
        return None
    # Check for valid hex
    if num_str.startswith('0x') or num_str.startswith('-0x'):

        # Positive hex 0xD32
        if num_str.startswith('0x'):
            num_str = num_str[2:]
            return conv_hex_helper(num_str)
        # Negative hex -0xD32
        else:
            num_str = num_str[3:]
            return conv_hex_helper(num_str) * (-1)

    # if decimal point appear only once and not hex
    if (num_str.count('.') == 1) and '0x' not in num_str:

        return conv_float_helper(num_str)

    # Check for valid integer
    if '.' not in num_str and 'x' not in num_str:
        return int_conv(num_str)

    return None


def int_conv(num_str):
    """Helper function for conv_num that converts an integer string
    to an integer.
    """
    nums = "1234567890"
    negative = 1
    res = 0
    if len(num_str) == 1 and num_str[0] not in nums:
        return None
    for i in range(len(num_str)):
        if i == 0 and num_str[i] == '-':
            negative = -1
            continue
        if num_str[i] in nums:
            res = res * 10 + (ord(num_str[i]) - 48)
        else:
            return None
    return res * negative


def int_conv(num_str):
    """Helper function for conv_num that converts an integer string
    to an integer.
    """
    nums = "1234567890"
    negative = 1
    res = 0
    if len(num_str) == 1 and num_str[0] not in nums:
        return None
    for i in range(len(num_str)):
        if i == 0 and num_str[i] == '-':
            negative = -1
            continue
        if num_str[i] in nums:
            res = res * 10 + (ord(num_str[i]) - 48)
        else:
            return None
    return res * negative


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
    if is_leap_year(year):
        days_in_months["02"] += 1
    day = 0
    for month in days_in_months:
        if day_count == 0:
            return "12-31-" + str(year-1)
        while day < days_in_months[month]:
            day += 1
            day_count -= 1
            if day_count == 0:
                day_str = str(day)
                if len(day_str) == 1:
                    day_str = "0" + day_str
                return month + "-" + day_str + "-" + str(year)

        if day_count == 0:
            return month + "-" + str(day) + "-" + str(year)
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
            if not is_leap_year(year):
                year += 1
                day_count = 0
    return (year, day_count)


def is_leap_year(year):
    """Returns True if integer year is a leap year and False if not."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def conv_endian(num, endian='big'):
    """Takes an integer value 'num' and converts it to a hexadecimal
    number. Endian type is determined by the flag 'endian'. Number is
    converted and returned as a string.
    """
    # check correct endian
    if endian != 'big' and endian != 'little':
        return None

    decimal_to_hex = {
      0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6",
      7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D",
      14: "E", 15: "F"
    }
    # Create a list of all individual hex digits
    quotients = []
    abs_num = abs(num)

    while abs_num > 15:
        quotients.append(decimal_to_hex[abs_num % 16])
        abs_num = abs_num // 16
    quotients.append(decimal_to_hex[abs_num])
    if len(quotients) % 2 != 0:
        quotients.append("0")

    # create a string of space separated hex bytes
    hex_bytes = hex_bits_to_byte(quotients, endian)

    # return the hex string based on sign.
    if num >= 0:
        return hex_bytes
    else:
        return "-" + hex_bytes


def hex_bits_to_byte(bit_list, endian):
    """Helper method that returns a string of space separated bytes
     from the given parameter bit_list"""

    # convert strings to bits and combine bits based on endian
    hex_num = ""
    while len(bit_list) > 0:
        first = bit_list.pop(0)
        second = bit_list.pop(0)
        if endian == "big":
            hex_num = second + first + " " + hex_num
        elif endian == "little":
            hex_num += second + first + " "
    return hex_num[:-1]
