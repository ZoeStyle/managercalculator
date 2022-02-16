import unittest
from src.domain.entities.equation import equation


class test_equation(unittest.TestCase):

    def test_equation_is_invalid(self):
        result = equation(0, 10, 80)
        self.assertEqual(result['status'], False)
        self.assertEqual(result['message'],
                         "It's not a quadratic equation!")

    def test_equation_delta_less_than_0(self):
        result = equation(10, 1, 80)
        self.assertEqual(result['status'], False)
        self.assertEqual(result['message'],
                         'The values entered are not real roots')

    def test_equation_value_b_and_c_than_0(self):
        result = equation(1, 0, 0)
        self.assertEqual(result['status'], False)
        self.assertEqual(result['message'],
                         'ValueB and valueC are set to zero')

    def test_equation_valid(self):
        result = equation(1, 10, 5)
        self.assertEqual(result['status'], True)
        self.assertEqual(result['message'], {
            'x1': -0.53,
            'x2': -9.47
        })


if __name__ == '__main__':
    unittest.main()
