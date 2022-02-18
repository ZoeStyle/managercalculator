import unittest
from src.domain.handlers.bhaskara_handler import bhaskara_handle


class bhaskara_handler(unittest.TestCase):

    def test_invalid_request(self):
        result = bhaskara_handle(None, 1)
        self.assertEqual(result['status'], False)
        self.assertEqual(
            result['message'],
            'It is mandatory to inform the valueA and valueB and valueC')

    def test_invalid_parameters(self):
        dict = {
            'valueA': 10,
            'valueB': 5
        }
        result = bhaskara_handle(dict, 1)
        self.assertEqual(result['status'], False)
        self.assertEqual(
            result['message'],
            'It is necessary to inform something in the request')


if __name__ == '__main__':
    unittest.main()
