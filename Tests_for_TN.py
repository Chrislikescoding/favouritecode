from unittest import TestCase, main # for all examples
from Test_numbers import find_target_sum


class TestTargetSum1(TestCase):
#1 pin should be an int
    def test_happy_valid(self):
        expected = {11, -1}
        result = set(find_target_sum( [3, 5, -4, 8, 11, 1, -1], 10))
        self.assertEqual(expected, result)


    def test_another_pair(self):
        expected = [24, 51]
        result = find_target_sum([1, 2, 4, 2, 1, 45, 51, 24], 75)
        self.assertEqual(expected, result)

    def test_no_pair(self):
        expected = None
        result = find_target_sum([1, 2, 4, 2, 1, 45, 51, 24], 76)
        self.assertEqual(expected, result)


    def test_in_sum_error(self):
        expected = {11, -1}
        result = set(find_target_sum( ['A', 5, -4, 8, 11, 1, -11], 8))
        self.assertEqual(expected, result)

# numbers = [3, 5, -4, 8, 11, 1, -1]
# target = 10
# result = find_target_sum1(numbers, target)





