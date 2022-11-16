import unittest
from task import conv_num, my_datetime, conv_endian


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test_conv_num_valid(self):
        """Tests for valid return value of function conv_num."""
        self.assertEqual(conv_num('0'), 0)

    def test_my_datetime(self):
        """Tests for valid return of function my_datetime."""
        self.assertEqual(my_datetime(0), '01-01-1970')

    def test_conv_endian(self):
        """Tests for valid return of function conv_endian."""
        self.assertEqual(conv_endian(0), "00")


if __name__ == '__main__':
    unittest.main()
