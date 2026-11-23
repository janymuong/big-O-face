"""
maximum subarray
https://leetcode.com/problems/maximum-subarray/description/
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = cur = nums[0]
        for x in nums[1:]:
            cur = max(x, cur + x)
            best = max(best, cur)
        return best

# if __name__ == "__main__":
#     sol = Solution()
#     # quick manual check while iterating
#     print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
#     print(sol.maxSubArray([1]))
#     print(sol.maxSubArray([5,4,-1,7,8]))
