import unittest
from more_fun_with_collections import set_membership


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertEqual(set_membership.in_set('d'), True)


class TestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertEqual(set_membership.in_set('t'), False)


if __name__ == '__main__':
    unittest.main()
