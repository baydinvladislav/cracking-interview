# Week 1 - Sequences
+ [Two Sum](#two-sum)
+ [Contains Duplicate](#contains-duplicate)
+ [Best Time to Buy and Sell Stock](#best-time-to-buy-and-sell-stock)
+ [Valid Anagram](#valid-anagram)
+ [Valid Parentheses](#valid-parentheses)
+ [Product of Array Except Self](#product-of-array-except-self)
+ [Maximum Subarray](#maximum-subarray)
+ [3Sum](#3sum)
+ [Merge Intervals](#merge-intervals)
+ [Group Anagrams](#group-anagrams)
+ [Maximum Product Subarray](#maximum-product-subarray)
+ [Search in Rotated Sorted Array](#earch-in-rotated-sorted-array)


## Two Sum
Дан неотсортированный массив чисел, вернуть индексы двух чисел сумма которых равна таргету.

https://leetcode.com/problems/two-sum/

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Идем по циклу, трекая порядковый номер итерации.</li>
 <li>Вычисляем попытку (target - nums[i]).</li>
 <li>Если попытки нет в словаре, то добавляем в словарь число текущей итерации.</li>
 <li>Если попытка в словаре, то вернуть индекс попытки из словаря (buffer[num]) и порядковый номер итерации цикла.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
```

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        buffer = {}
        for i, num in enumerate(nums):
            attempt = target - num
            if attempt not in buffer:
                buffer[num] = i
            else:
                return [buffer[attempt], i]

        return [-1, -1]
```

<details><summary>Test cases</summary><blockquote>

```python
import unittest


class TestTwoSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual([-1, -1], Solution().twoSum(nums=[], target=9))

    def test_first(self):
        self.assertEqual([0, 1], Solution().twoSum(nums=[2, 7, 11, 15], target=9))

    def test_second(self):
        self.assertEqual([1, 2], Solution().twoSum(nums=[3, 2, 4], target=6))

    def test_third(self):
        self.assertEqual([0, 1], Solution().twoSum(nums=[3, 3], target=6))

    def test_no_solution(self):
        self.assertEqual([-1, -1], Solution().twoSum(nums=[3, 3, 1, 4, 5], target=16))


if __name__ == "__main__":
    unittest.main()
```

</blockquote></details>


## Contains Duplicate
Дан массив чисел, вернуть True если в массиве есть дубликаты, вернуть False, если массив содержит только уникальные числа.

https://leetcode.com/problems/contains-duplicate/


<details><summary>Решение:</summary><blockquote>
Три решения:
<ol>
 <li>Отсортировать массив и идти по нему циклом сравнивая nums[i-1] и nums[i].</li>
 <li>Добавить все числа в словарь и отслеживать их частоту, если у кого больше чем  1, то значит был дубликат.</li>
 <li>Воспользоваться встроенной структурой set().</li>
</ol>

</blockquote></details>

```
Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

```python
from typing import List


class Solution:
    def containsDuplicate_additional_memory(self, nums: List[int]) -> bool:
        buffer = {}
        for num in nums:
            if num not in buffer:
                buffer[num] = 1
            else:
                return True
        return False

    def containsDuplicate_sorting(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False

    def containsDuplicate_set(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestContainsDuplicate(unittest.TestCase):
    def test_first(self):
        self.assertTrue(Solution().containsDuplicate_additional_memory(nums=[1, 2, 3, 1]))
        self.assertTrue(Solution().containsDuplicate_sorting(nums=[1, 2, 3, 1]))
        self.assertTrue(Solution().containsDuplicate_set(nums=[1, 2, 3, 1]))

    def test_second(self):
        self.assertFalse(Solution().containsDuplicate_additional_memory(nums=[1, 2, 3, 4]))
        self.assertFalse(Solution().containsDuplicate_sorting(nums=[1, 2, 3, 4]))
        self.assertFalse(Solution().containsDuplicate_set(nums=[1, 2, 3, 4]))

    def test_third(self):
        self.assertTrue(Solution().containsDuplicate_additional_memory(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
        self.assertTrue(Solution().containsDuplicate_sorting(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
        self.assertTrue(Solution().containsDuplicate_set(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == "__main__":
    unittest.main()
```

</blockquote></details>


## Best Time to Buy and Sell Stock
Дан массив с числами, каждое число представляет цену акции на iый день.
Найти день наилучший для покупки и день наилучший для продажи.
Вернуть наибольшую прибыль после продажи. Если прибыль получить невозможно вернуть 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Для решения задачи отслеживаем две переменные: max_profit и min_price.</li>
 <li>Если на итерации число меньше чем в min_price, то обновляем min_price текущим числом.</li>
 <li>Вычисляем прибыль, отнимая от числа на текущей итерации min_price.</li>
 <li>Обновляем max_profit числом из второго пункта, если прибыль получилась больше чем была.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

```python3 
class Solution:
    def maxProfit(self, prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestBestTimeBuyAndSellStock(unittest.TestCase):
    def test_first(self):
        self.assertEqual(5, Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))

    def test_second(self):
        self.assertEqual(0, Solution().maxProfit(prices=[7, 6, 4, 3, 1]))
```

</blockquote></details>


## Valid Anagram
Даны две строки. Вернуть True, если строки являются анаграмами, вернуть False в противном случае.
Анаграмма - это слово образованное от другого путем перестановки букв.

https://leetcode.com/problems/valid-anagram/

<details><summary>Решение:</summary><blockquote>
Два решения:
<ol>
 <li>Отсортировать две строки и сравнить их.</li>
 <li>Создать по словарю для каждой строки. Добавить символы первой строки и их частоту в первый словарь, также поступить и для второй строки и второго словаря. Сравнить два словаря.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
```


```python3
class Solution:
    def isAnagram_sorting(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram_additional_memory(self, s: str, t: str) -> bool:
        buffer_1, buffer_2 = {}, {}
        
        for char in s:
            buffer_1[char] = buffer_1.get(char, 0) + 1

        for char in t:
            buffer_2[char] = buffer_2.get(char, 0) + 1

        return buffer_1 == buffer_2
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestValidAnagram(unittest.TestCase):
    def test_first(self):
        self.assertTrue(5, Solution().isAnagram_sorting(s="anagram", t="nagaram"))
        self.assertTrue(5, Solution().isAnagram_additional_memory(s="anagram", t="nagaram"))

    def test_second(self):
        self.assertFalse(0, Solution().isAnagram_sorting(s="rat", t="car"))
        self.assertFalse(0, Solution().isAnagram_additional_memory(s="rat", t="car"))
```

</blockquote></details>


## Valid Parentheses
Дана строка в которой могу быть символы: '(', ')', '{', '}', '[', ']'.
Вернуть True, если скобочная последовательность в строке верная (открывающая скобка закрывается скобкой такого же типа и 
скобки закрываются в правильном порядке).

https://leetcode.com/problems/valid-parentheses/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Инициализировать словарь со скобками и пустой сткек.</li>
 <li>Идем циклом по входной строке.</li>
 <li>Если символ строке есть ключ в словаре скобок, то значит символ является открывающей скобкой, добавляем символ в стек.</li>
 <li>Если стек пуст или если из словаря по последнему элементу стека мы не получаем текущий элемент (нужная закрывающая скобка), значит скобочная последовательность не верная.</li>
 <li>Вернуть булево значение от пустого стека.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
```

```python3
from collections import deque


def isValid(s):
    parentheses = {'(': ')', '{': '}', '[': ']'}
    stack = deque()

    for symbol in s:
        if symbol in parentheses:
            stack.append(symbol)

        elif len(stack) == 0 or parentheses[stack.pop()] != symbol:
            return False

    return len(stack) == 0
```


<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestValidParentheses(unittest.TestCase):
    def test_first(self):
        self.assertTrue(Solution().isValid(s="()"))

    def test_second(self):
        self.assertTrue(Solution().isValid(s="()[]{}"))

    def test_third(self):
        self.assertFalse(Solution().isValid(s="(]"))
```

</blockquote></details>


## Product of Array Except Self
Дан массив чисел, вернуть новый массив содержащий перемножение всех элементов кроме iго элемента.
Решение должно быть за линейное время и без операции деления.

https://leetcode.com/problems/product-of-array-except-self/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Накапливаем префикс каждого элемента в результирующем массиве.</li>
 <li>Умножаем элемента результирующего массива на постфикс, проходя циклом с конца к началу.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

```python3
def productExceptSelf(nums):
    result = []

    prefix = 1
    for i in range(len(nums)):
        result.append(prefix)
        prefix *= nums[i]

    postfix = 1
    for i in reversed(range(len(nums))):
        result[i] *= postfix
        postfix *= nums[i]

    return result
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestProductArrayExceptSelf(unittest.TestCase):
    def test_first(self):
        self.assertEqual([24, 12, 8, 6], Solution().productExceptSelf(nums=[1, 2, 3, 4]))

    def test_second(self):
        self.assertEqual([0, 0, 9, 0, 0], Solution().productExceptSelf(nums=[-1, 1, 0, -3, 3]))
```
</blockquote></details>

## Maximum Subarray
Вернуть самую большую сумму подмассива.

https://leetcode.com/problems/maximum-subarray/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Проходим первый раз по циклу и перемножаем элементы, сохраняем макс.произведение чисел, если натыкаемся на 0, то начинаем накапливать произведение заново.</li>
 <li>Делаем тоже самое, но в этот раз проходим массив с конца к началу.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
```

```python3
def maxProduct(nums):
    answer = nums[0]
    product = 0
    for i in range(len(nums)):
        if product == 0:
            product = nums[i]
        else:
            product *= nums[i]
        answer = max(answer, product)

    product = 0
    for i in range(len(nums) - 1, -1, -1):
        if product == 0:
            product = nums[i]
        else:
            product *= nums[i]
        answer = max(answer, product)
    return answer
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestMaxProduct(unittest.TestCase):
    def test_first(self):
        self.assertEqual(6, Solution().maxProduct(nums=[2, 3, -2, 4]))

    def test_second(self):
        self.assertEqual(0, Solution().maxProduct(nums=[-2, 0, -1]))
```

</blockquote></details>


## 3Sum
Для массива целых чисел nums вернуть все триплеты [nums[i], nums[j], nums[k]] такие, что i != j, i != k и j != k, и nums[i] + nums[j] + nums[k] == 0. Обратите внимание, что в наборе решений не должно быть повторяющихся триплетов.

https://leetcode.com/problems/3sum/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Сортируем входной массив.</li>
 <li>Проходим циклом по массиву, пропуская дубликаты.</li>
 <li>Необходимо для каждого числа на итерации цикла найти два таких числа сумма которых будет равна отрицательному числу на итерации, для этого используем метод двух указателей.</li>
 <li>Если два числа дают в суммме отрицательное число, то добавить 3 числа (число итерации и два числа под указателями) в ответ.</li>
 <li>Если сумма меньше, то сдвинуть левый указатель к концу.</li>
 <li>Если сумма больше, то сдвинуть правый указатель к началу.</li>
 <li>Вернуть массив троек.</li>
</ol>
</blockquote></details>


```
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
```


```python3
class Solution:
    def threeSum(self, nums):
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            if nums[i - 1] == nums[i]:
                continue

            self.search_pair(nums, triplets, left=i + 1, target_sum=-nums[i])
        return triplets

    def search_pair(self, arr, triplets, left, target_sum):
        right = len(arr) - 1
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target_sum:
                triplets.append([-target_sum, arr[left], arr[right]])
                left += 1
                right -= 1

                # skip duplicates
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif current_sum < target_sum:
                left += 1

            elif current_sum > target_sum:
                right -= 1
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestProductArrayExceptSelf(unittest.TestCase):
    def test_first(self):
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]))

    def test_second(self):
        self.assertEqual([], Solution().threeSum(nums=[]))

    def test_third(self):
        self.assertEqual([], Solution().threeSum(nums=[0]))
```

</blockquote></details>


## Merge Intervals
Дан массив интервалов, смержить все пересекающиеся интервалы и вернуть массив не пересекающихся интервалов.

https://leetcode.com/problems/merge-intervals/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Отсортировать интервалы по их началу.</li>
 <li>Берем за точку отсчета первый интервал из массива.</li>
 <li>Цикл по массиву со второго элемента.</li>
 <li>Если конец предыдущего интервала больше чем начало последующего, то интервалы пересекаются, берем за конец интервала больший конец двух интервалов.</li>
 <li>В случае, если интервалы не пересекаются, то добавляем интервал в результирующий массив и обновляем начало и конец интервала значениями данного интервала.</li>
 <li>После цикла нужно будет добавить последний интервал в результирующий массив.</li>
 <li>Вернуть результирующий массив.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

```python3
def merge(intervals):
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x[0])
    merged_intervals = []

    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if end >= interval[0]:
            end = max(interval[1], end)
        else:
            merged_intervals.append([start, end])
            start = interval[0]
            end = interval[1]

    merged_intervals.append([start, end])
    return merged_intervals
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestMergeIntervals(unittest.TestCase):
    def test_first(self):
        self.assertEqual([[1, 6], [8, 10], [15, 18]], Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))

    def test_second(self):
        self.assertEqual([[1, 5]], Solution().merge(intervals=[[1, 4], [4, 5]]))
```

</blockquote></details>

## Group Anagrams
Дан массив слов, сгруппировать анаграммы в массивах.

https://leetcode.com/problems/group-anagrams/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Иницализовать словарь с пустым листом в значении.</li>
 <li>Сортируем каждое слово.</li>
 <li>Преобразуем отсортированное слово в кортеж (т.к. он может быть ключом, потому что неизменяемый тип данных).</li>
 <li>Добавляем кортеж как ключ в словарь.</li>
 <li>Проходя циклом по входному массиву слов, смотрим если слово совпадает с ключом (кортежем) то добавляем это слово в массив под этим ключом.</li>
 <li>Вернуть значения наполненного словаря.</li>
</ol>
</blockquote></details>

```
Example 1
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
```

```python3
from collections import defaultdict


def groupAnagrams(strs):
    if not strs:
        return [[""]]

    hash_map = defaultdict(list)
    for word in strs:
        hash_map[tuple(sorted(word))].append(word)
    return list(hash_map.values())
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestMaxProduct(unittest.TestCase):
    def test_first(self):
        output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertEqual(output, Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))

    def test_second(self):
        self.assertEqual([[""]], Solution().groupAnagrams(strs=[""]))

    def test_third(self):
        self.assertEqual([["a"]], Solution().groupAnagrams(strs=["a"]))```
```
</blockquote></details>



## Maximum Product Subarray
Дан массив чисел. Вернуть максимальное произведение подмассивов.

https://leetcode.com/problems/maximum-product-subarray/

```
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

```python3

```


## Search in Rotated Sorted Array
Дан массив числе отсортированный по возрастанию и развернутый относительно одного указателя.
Вернуть индекс таргета, если его нет вернуть -1.
Решение за O(log n).

https://leetcode.com/problems/search-in-rotated-sorted-array/

```
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
```

```python3

```


