"""
first unique character in a string
https://leetcode.com/problems/first-unique-character-in-a-string/description/
"""
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # count = {}
        # for c in s:
        #     count[c] = count.get(c, 0) + 1
        # for i, c in enumerate(s):
        #     if count[c] == 1:
        #         return i
        # return -1  
        counts = Counter(s)
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1


# s = "loveleetcode"
# s1 = "aabb"

# print(Solution().firstUniqChar(s))
# print(Solution().firstUniqChar(s1))
    
