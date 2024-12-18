import unittest


class Solution:
    def search(self, nums, target):

        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1

        def search(left, right):
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1

        n = len(nums)

        if n == 1:
            return 0 if nums[0] == target else -1

        rotate_index = find_rotate_index(0, n - 1)

        # if target is the smallest element
        if nums[rotate_index] == target:
            return rotate_index

        # if array is not rotated, search in the entire array
        if rotate_index == 0:
            return search(0, n - 1)

        if target < nums[0]:
            # search on the right side
            return search(rotate_index, n - 1)

        # search on the left side
        return search(0, rotate_index)

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def searchOnePass(self, nums, target):
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            elif nums[start] > nums[mid]:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1


class TestMaxProduct(unittest.TestCase):
    def test_first(self):
        self.assertEqual(4, Solution().searchTwoPass(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
        self.assertEqual(4, Solution().searchOnePass(nums=[4, 5, 6, 7, 0, 1, 2], target=0))

    def test_second(self):
        self.assertEqual(-1, Solution().searchTwoPass(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
        self.assertEqual(-1, Solution().searchOnePass(nums=[4, 5, 6, 7, 0, 1, 2], target=3))

    def test_third(self):
        self.assertEqual(-1, Solution().searchTwoPass(nums=[1], target=0))
        self.assertEqual(-1, Solution().searchOnePass(nums=[1], target=0))


if __name__ == "__main__":
    unittest.main()
