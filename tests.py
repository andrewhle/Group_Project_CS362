import unittest
from task import conv_num, my_datetime, conv_endian


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    ############################################################
    #
    # conv_num Tests
    #
    ############################################################

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

    ############################################################
    #
    # my_datetime Tests
    #
    ############################################################

    def test_my_datetime(self):
        """Tests for valid return of function my_datetime."""
        self.assertEqual(my_datetime(0), '01-01-1970')

    ############################################################
    #
    # conv_endian Tests
    #
    ############################################################

    def test_conv_endian(self):
        """Tests for valid return of function conv_endian."""
        self.assertEqual(conv_endian(0), "00")


if __name__ == '__main__':
    unittest.main()
