from unittest import TestCase
# from itertools import combinations
#
#
# def find_pairs(li, n):
#     for i, j in combinations(li, 2):
#         if abs(i-j) == n:
#             return i, j


class TestFindPairs(TestCase):
    def test_easy(self):
        expected = {51, 45}
        result = set(find_pairs([1, 2, 4, 2, 1, 45, 51, 24], 6))
        self.assertEqual(expected, result)

    def test_hard(self):
        expected = {45, 24}
        result = set(find_pairs([1, 2, 4, 2, 1, 45, 51, 24], 21))
        self.assertEqual(expected, result)

    def test_no_pair(self):
        expected = None
        result = find_pairs([1, 2, 4, 2, 1, 45, 51, 24], 60)
        self.assertEqual(expected, result)
