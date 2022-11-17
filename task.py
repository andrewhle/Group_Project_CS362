def conv_num(num_str):
    """Takes a string and converts it to a base 10 number then
    returns it. Can handle strings representing integer, float,
    and hexadecimal string representations of numbers.
    """
    if not num_str:
        return None
    nums = "1234567890"
    # Check for valid integer
    if '.' not in num_str and 'x' not in num_str:
        res = 0
        negative = 1
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
    return "01-01-1970"


def conv_endian(num, endian='big'):
    """Takes an integer value 'num' and converts it to a hexamdecimal
    number. Endian type is determined by the flag 'endian'. Number is
    converted and returned as a string.
    """
    return "00"
