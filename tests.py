import unittest
from task import conv_num, my_datetime, conv_endian
from datetime import datetime, timezone
from random import randrange, choice


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

##################################################
#
# Tests for conv_num
#
##################################################

    def test_conv_num_valid(self):
        """Tests for valid return value of function conv_num."""
        self.assertEqual(conv_num('0'), 0)

    def test_conv_num_empty_input(self):
        """Tests that empty string input returns None."""
        self.assertIsNone(conv_num(""))

    def test_conv_num_not_string(self):
        """Tests that non-string input returns None."""
        self.assertIsNone(conv_num(5))

    def test_conv_num_int5(self):
        """Tests that input of '5' returns 5."""
        self.assertEqual(conv_num("5"), 5)

    def test_conv_num_int23(self):
        """Tests that input of '23' returns 23."""
        self.assertEqual(conv_num("23"), 23)

    def test_conv_num_int0001(self):
        """Tests that input of '0001' returns 1."""
        self.assertEqual(conv_num("0001"), 1)

    def test_conv_num_intneg_0001(self):
        """Tests that input of '-0001' returns -1."""
        self.assertEqual(conv_num("-0001"), -1)

    def test_conv_num_neg_int(self):
        """Tests that input of '-845' returns -845."""
        self.assertEqual(conv_num("-845"), -845)

    def test_conv_num_invalid_char_space(self):
        """Tests that input of ' 1' returns None."""
        self.assertIsNone(conv_num(" 1"))

    def test_conv_num_invalid_char_space2(self):
        """Tests that input of '1 ' returns None."""
        self.assertIsNone(conv_num("1 "))

    def test_conv_num_invalid_char(self):
        """Tests that input of '1234a89' returns None."""
        self.assertIsNone(conv_num("1234a89"))

    def test_conv_num_invalid_char2(self):
        """Tests that input of '@' returns None."""
        self.assertIsNone(conv_num("@"))

    def test_conv_num_invalid_neg_sign(self):
        """Tests that input of '--845' returns None."""
        self.assertIsNone(conv_num("--845"))

    def test_conv_num_invalid_neg_sign2(self):
        """Tests that input of '-845-' returns None."""
        self.assertIsNone(conv_num("-845-"))

    def test_conv_num_invalid_neg_sign3(self):
        """Tests that input of '-' returns None."""
        self.assertIsNone(conv_num("-"))

    def test_conv_num_int_returned(self):
        """Tests that return value is of type int"""
        self.assertTrue(isinstance(conv_num("1"), int))

    def test_conv_num_float_invalid1(self):
        """Tests that input of '1.2.3.4' returns None."""
        self.assertIsNone(conv_num("1.2.3.4"))

    def test_conv_num_float_invalid2(self):
        """Tests that input of '-2.-2' returns None."""
        self.assertIsNone(conv_num("-2.-2"))

    def test_conv_num_float_invalid3(self):
        """Tests that input of '2.2a' returns None."""
        self.assertIsNone(conv_num("2.2a"))

    def test_conv_num_float_invalid4(self):
        """Tests that input of '2. 2' returns None."""
        self.assertIsNone(conv_num("2. 2"))

    def test_conv_num_float1(self):
        """Tests that input of '-123.45' returns -123.45."""
        self.assertEqual(conv_num("-123.45"), -123.45)

    def test_conv_num_float2(self):
        """Tests that input of '.45' returns .45."""
        self.assertEqual(conv_num(".45"), .45)

    def test_conv_num_float3(self):
        """Tests that input of '123.' returns 123.0."""
        self.assertEqual(conv_num("123."), 123.0)

    def test_conv_num_hex1(self):
        """Tests that input of '0x123G' returns None"""
        self.assertIsNone(conv_num("0x123G"))

    def test_conv_num_hex2(self):
        """Tests that input of '0xAD4' returns 2772"""
        self.assertEqual(conv_num("0xAD4"), 2772)

    def test_conv_num_hex3(self):
        """Tests that input of '0xAZ4' returns None"""
        self.assertIsNone(conv_num("0xAZ4"))

    def test_conv_num_hex4(self):
        """Tests that input of '0x AZ4' returns None"""
        self.assertIsNone(conv_num("0x AZ4"))

    def test_random_hex(self):
        """Random tests for converting hex strings"""
        pass_test = True
        chars = "1234567890ABCDEF"
        for _ in range(100):
            t = "0x"
            length = randrange(1, 10)
            for _ in range(length):
                t += choice(chars)
            expected = eval(t)
            result = conv_num(t)
            if expected != result:
                pass_test = False
        self.assertTrue(pass_test)

##################################################
#
# Tests for my_datetime
#
##################################################

    def test_my_datetime_1(self):
        """Tests for valid return of function my_datetime."""
        self.assertEqual(my_datetime(0), '01-01-1970')

    def test_my_datetime_2(self):
        """Tests that 1234567891 returns '02-13-2009'."""
        self.assertEqual(my_datetime(1234567891), '02-13-2009')

    def test_my_datetime_3(self):
        """Tests that 999999 returns '01-12-1970'."""
        self.assertEqual(my_datetime(999999), '01-12-1970')

    def test_my_datetime_4(self):
        """Tests that 99999999 returns '03-03-1973'."""
        self.assertEqual(my_datetime(99999999), '03-03-1973')

    def test_my_datetime_5(self):
        """Tests that 999999999 returns '09-09-2001'."""
        self.assertEqual(my_datetime(999999999), '09-09-2001')

    def test_my_datetime_6(self):
        """Tests that 123456789 returns '11-29-1973'."""
        self.assertEqual(my_datetime(123456789), '11-29-1973')

    def test_my_datetime_7(self):
        """Tests that 9876543210 returns '12-22-2282'."""
        self.assertEqual(my_datetime(9876543210), '12-22-2282')

    def test_my_datetime_8(self):
        """Tests that 201653971200 returns '02-29-8360'."""
        self.assertEqual(my_datetime(201653971200), '02-29-8360')

    def test_my_datetime_9(self):
        """Tests that 951807600 returns '02-29-2000'."""
        self.assertEqual(my_datetime(951807600), '02-29-2000')

    def test_my_datetime_10(self):
        """Tests that 951894000 returns '03-01-2000'."""
        self.assertEqual(my_datetime(951894000), '03-01-2000')

    def test_my_datetime_11(self):
        """Tests that 1078124400 returns '03-01-2004'."""
        self.assertEqual(my_datetime(1078124400), '03-01-2004')

    def test_my_datetime_12(self):
        """Tests that 1078038000 returns '02-29-2004'."""
        self.assertEqual(my_datetime(1078038000), '02-29-2004')

    def test_my_datetime_13(self):
        """Tests that 2529730800 returns '03-01-2050'."""
        self.assertEqual(my_datetime(2529730800), '03-01-2050')

    def test_my_datetime_14(self):
        """Tests that 2529644400 returns '02-28-2050'."""
        self.assertEqual(my_datetime(2529644400), '02-28-2050')

    def test_random_datetime(self):
        """"""
        pass_test = True
        for _ in range(1000):
            tstamp = randrange(0, 10000000000)
            expected = datetime.fromtimestamp(
                tstamp, tz=timezone.utc).strftime("%m-%d-%Y")
            result = my_datetime(tstamp)
            if expected != result:
                pass_test = False
        self.assertTrue(pass_test)

##################################################
#
# Tests for conv_endian
#
##################################################

    def test_conv_endian(self):
        """Tests for valid return of function conv_endian."""
        self.assertEqual(conv_endian(0), "00")

    def test_conv_endian1(self):
        """Tests for invalid endian parameter"""
        self.assertIsNone(conv_endian(0, 'small'))

    def test_conv_endian2(self):
        """Tests for big endian int"""
        expected = '0E 91 A2'
        result = conv_endian(954786, 'big')
        self.assertEquals(expected, result)

    def test_conv_endian3(self):
        """Tests for little endian positive int"""
        expected = "A2 91 0E"
        result = conv_endian(954786, "little")
        self.assertEqual(expected, result)

    def test_con_endian4(self):
        """Tests for big endian negative int"""
        expected = '-0E 91 A2'
        result = conv_endian(-954786, 'big')
        self.assertEquals(expected, result)

    def test_conv_endian5(self):
        """Tests for big endian negative int"""
        expected = '-A2 91 0E'
        result = conv_endian(-954786, 'little')
        self.assertEquals(expected, result)

    def test_conv_endian6(self):
        """Tests for little endian negative int"""
        expected = "-34"
        result = conv_endian(-52, "little")
        self.assertEqual(expected, result)

    def test_conv_endian7(self):
        """Tests for big endian negative int"""
        expected = "-02 09"
        result = conv_endian(-521, "big")
        self.assertEqual(expected, result)

    def test_conv_endian8(self):
        """Tests for little endian negative int"""
        expected = "-09 02"
        result = conv_endian(-521, "little")
        self.assertEqual(expected, result)

    def test_conv_endian9(self):
        """Tests for little endian negative int"""
        expected = "-A2 91 0E"
        result = conv_endian(num=-954786, endian='little')
        self.assertEqual(expected, result)

    def test_conv_endian10(self):
        """Tests for invalid input"""
        self.assertIsNone(conv_endian(num=-954786, endian='small'))


if __name__ == '__main__':
    unittest.main()
