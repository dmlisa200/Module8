import unittest
from more_fun_with_collections.set_membership import in_set


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertEqual(set_membership.in_set(num), True)


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertEqual(set_membership.in_set(num), False)


if __name__ == '__main__':
    unittest.main()
