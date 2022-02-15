import unittest
from main import path_finder


class MyTestCase(unittest.TestCase):
    def test_return_list(self):
        self.assertTrue(isinstance(path_finder([0, 0], [1, 1]), list))

    def test_correct_input(self):
        self.assertRaises(TypeError, path_finder([0, 0], [1, 1]))

    def test_two_elements(self):
        self.assertRaises(TypeError, path_finder([0, 0], [1, 1]))

    def test_all_int(self):
        self.assertRaises(TypeError, path_finder([0, 0], [1, 1]))

    def test_time_exception(self):
        self.assertRaises(TypeError, path_finder([0, 0], [359, 178]))


if __name__ == '__main__':
    unittest.main()
