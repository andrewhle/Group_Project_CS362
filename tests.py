import unittest
from task import conv_num, my_datetime, conv_endian


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

    def test_conv_num_int5(self):
        """Tests that input of '5' returns 5."""
        self.assertEqual(conv_num("5"), 5)

    def test_conv_num_int23(self):
        """Tests that input of '23' returns 23."""
        self.assertEqual(conv_num("23"), 23)

    def test_conv_num_neg_int(self):
        """Tests that input of '-845' returns -845."""
        self.assertEqual(conv_num("-845"), -845)

    def test_conv_num_invalid_char(self):
        """Tests that input of '1234a89' returns None."""
        self.assertIsNone(conv_num("1234a89"))

    def test_conv_num_invalid_neg_sign(self):
        """Tests that input of '--845' returns None."""
        self.assertIsNone(conv_num("--845"))

    def test_conv_num_int_returned(self):
        """Tests that return value is of type int"""
        self.assertTrue(isinstance(conv_num("1"), int))

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


if __name__ == '__main__':
    unittest.main()
