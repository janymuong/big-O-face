"""
valid parentheses
https://leetcode.com/problems/valid-parentheses/description/
"""


class Solution:
    def isValid(self, s: str,) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in pairs: # closing bracket
                if not stack or stack.pop() != pairs[char]:
                    return False
            else: # opening bracket
                stack.append(char)
        return not stack # leftovers mean unclosed




# run through test cases;

# s1 = "()"
# s2 = "()[]{}"
# s3 = "(]"
# s4 = "([])"
# s5 = "([)]"
