import unittest
class Countdigit_test(unittest.TestCase):
    def test_countdigit(self):
        num_list = [1, 1, 3, 2, 1, 3, 4]
        self.assertEqual(num_list.count(1), 3)
        self.assertEqual(num_list.count(2), 1)
        self.assertEqual(num_list.count(3), 2)
        self.assertEqual(num_list.count(4), 1)
if __name__ == '__main__':
    unittest.main()