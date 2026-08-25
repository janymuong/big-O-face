"""
find the index of the first occurrence in a string
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        if m > n:
            return -1

        for start in range(n - m + 1):
            if haystack[start:start + m] == needle:
                return start

        return -1


if __name__ == "__main__":
     sol = Solution()
     print(sol.strStr("sadbutsad", "sad"))    # 0
     print(sol.strStr("leetcode", "leeto"))   # -1
