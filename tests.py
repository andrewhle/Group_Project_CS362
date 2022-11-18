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


if __name__ == '__main__':
    unittest.main()
