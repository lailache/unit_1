import unittest

from main import process_data


class TestMain(unittest.TestCase):

    def test_process_data(self):
        input_data = [['1', '2', '3'], ['4', '5', '6']]
        expected_output = [['2', '4', '6'], ['8', '10', '12']]
        self.assertEqual(process_data(input_data), expected_output)
