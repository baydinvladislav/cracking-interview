"""
Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
Надо вернуть [1, 2, 2, 3] (порядок неважен).

Фактически нам нужно вернуть пересечение множеств, но с повторением элементов.
"""


def f(nums1, nums2):
    d = {}
    res = []
    for num in nums1:
        if num not in d:
            d[num] = 0
        d[num] += 1

    for num in nums2:
        if num in d:
            d[num] -= 1
            res.append(num)

            if num[d] == 0:
                del num[d]

    return res


class Solution:
    def find_intersections(self, l1, l2):
        result = []
        for number in l1:
            if number in l2:
                result.append(number)
        return result

    def find_intersections_const_space(self, l1, l2):
        for i in range(len(l1)):
            if l1[i] not in l2:
                l1.pop(i)  # or use l1.remove(number)
        return l1


print(Solution().find_intersections_const_space(l1=[1, 2, 3, 2, 0], l2=[5, 1, 2, 7, 3, 2]))


# Time Complexity: O(n * m)
# Space Complexity: O(n) - n is length of the smallest array
def solution(arr1, arr2):
    buffer = {}
    if arr1 > arr2:
        arr1, arr2 = arr2, arr1

    for item in arr1:
        if item in arr2:
            arr2.remove(item)

            if item not in buffer:
                buffer[item] = 0
            buffer[item] += 1

    result = []
    for key, value in buffer.items():
        while value > 0:
            result.append(key)
            value -= 1

    return result


def test_first():
    arr1 = [1, 2, 3]
    arr2 = [1, 2]
    expect = [1, 2]

    assert expect == solution(arr1, arr2)


def test_second():
    arr1 = [1, 2, 3, 2, 0]
    arr2 = [5, 1, 2, 7, 3, 2]
    expect = [1, 2, 2, 3]

    assert expect == solution(arr1, arr2)


def test_third():
    arr1 = [1, 2, 3]
    arr2 = [1, 1]
    expect = [1]

    assert expect == solution(arr1, arr2)


def test_fourth():
    arr1 = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [1, 3, 3, 5, 7, 9]
    expect = [1, 3, 3, 5, 7, 9]

    assert expect == solution(arr1, arr2)


def test_fifth():
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
    arr2 = [1, 6, 6, 8, 8]
    expect = [1, 6, 8, 8]

    assert expect == solution(arr1, arr2)
