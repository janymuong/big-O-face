"""
valid anagram
https://leetcode.com/problems/valid-anagram/description/
"""
from collections import Counter

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        ''' check if two strings are anagrams of each other
        we use the Counter gets me a dictionary of the counts of each character in the string
        and then we compare the two dictionaries to see if they are equal
        :param s: first string
        :param t: second string
        :return: True if the two strings are anagrams of each other, False otherwise
        '''
        return Counter(s) == Counter(t)




# if __name__ == "__main__":
#     sol = Solution()
#     # quick manual check while iterating
#     print(sol.is_anagram("listen", "silent"))