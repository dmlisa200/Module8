import unittest
from more_fun_with_collections import assign_average


class MyTestCase(unittest.TestCase):
    def test_A_value(self):
        self.assertEqual(assign_average.switch_average('A'), 'Ankeny')

    def test_B_value(self):
        self.assertEqual(assign_average.switch_average('B'), 'Ames')

    )


if __name__ == '__main__':
    unittest.main()
