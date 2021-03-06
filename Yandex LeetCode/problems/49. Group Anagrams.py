"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""


from collections import defaultdict


class Solution:
    # Time Complexity: O(NK log K). Where N is the length of strs, and K is the maximum length of a string in strs.
    # Space Complexity: O(NK)
    def groupAnagrams(self, strs):
        """
        1. Sort the word alphabetically.
        2. Insert sorted word into tuple data structure because tuple can be a key at a dict.
        3. Insert a tuple into the dict data structure as a key, now we have a dictionary like this: {tuple: []}
        4. Insert a word to value array.
        5. Return only values from dict without their keys.
        """
        char_map = defaultdict(list)
        for word in strs:
            sorted_word = sorted(word)
            key = tuple(sorted_word)
            char_map[key].append(word)
        return char_map.values()


print(Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
