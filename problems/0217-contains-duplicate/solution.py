#!/usr/bin/env python
"""
contains duplicate
https://leetcode.com/problems/contains-duplicate
"""


# from collections import Counter

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        check if the list contains duplicate elements
        :param nums: list of integers
        :return: True if the list contains duplicate elements, False otherwise
        """
        # counter = Counter(nums)
        seen = set() # set data structure to store unique elements/doesnt allow duplicates
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False



# nums1 = [1,1,1,3,3,4,3,2,4,2]
# nums2 = [1,2,3,4]
# sol = Solution()
# print(sol.containsDuplicate(nums1))  # True
# print(sol.containsDuplicate(nums2))  # False

