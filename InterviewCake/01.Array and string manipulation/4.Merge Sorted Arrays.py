import unittest


# my code based on their solution
# Time Complexity: O(n)
# Space Complexity: O(n)
def merge_lists(my_list, alices_list):
    result = [None] * (len(my_list) + len(alices_list))

    p1 = p2 = 0
    for i in range(len(result)):
        first_is_exhausted = p1 >= len(my_list)
        second_is_exhausted = p2 >= len(alices_list)

        if not first_is_exhausted and (second_is_exhausted or my_list[p1] < alices_list[p2]):
            result[i] = my_list[p1]
            p1 += 1
        else:
            result[i] = alices_list[p2]
            p2 += 1

    return result


# their solution
# Time Complexity: O(n)
# Space Complexity: O(n)
def merge_lists(my_list, alices_list):
    result = [None] * (len(my_list) + len(alices_list))
    current_my_list_idx = current_alices_list_idx = current_result_idx = 0
    while current_result_idx < len(result):
        is_my_list_exhausted = current_my_list_idx == len(my_list)
        is_alices_list_exhausted = current_alices_list_idx == len(alices_list)
        if not is_my_list_exhausted and \
                (is_alices_list_exhausted or my_list[current_my_list_idx] < alices_list[current_alices_list_idx]):
            result[current_result_idx] = my_list[current_my_list_idx]
            current_my_list_idx += 1
        else:
            result[current_result_idx] = alices_list[current_alices_list_idx]
            current_alices_list_idx += 1

        current_result_idx += 1

    return result


class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
