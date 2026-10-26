"""
valid palindrome
https://leetcode.com/problems/valid-palindrome/description/
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()] # letters and digits
        return cleaned == cleaned[::-1] # compare the cleaned list with its reverse

# s = "A man, a plan, a canal: Panama"
# print(Solution().isPalindrome(s))