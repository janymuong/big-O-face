"""
binary search
https://leetcode.com/problems/binary-search/description/
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


# nums = [-1,0,3,5,9,12]; target = 2
# search = Solution().search(nums, target)
# print(search)
