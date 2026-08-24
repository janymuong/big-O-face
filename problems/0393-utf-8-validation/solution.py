"""
utf-8 validation
https://leetcode.com/problems/utf-8-validation/
"""
from typing import List 


class Solution:
    '''solves the problem of validating UTF-8 encoding for a given list of integers representing bytes.
    '''
    def validUtf8(self, data: List[int]) -> bool:
        # number of continuation bytes expected for the current character
        need = 0

        for byte in data:
            # We only care about the least significant 8 bits
            b = byte & 0xFF

            if need == 0:
                # determine the number of bytes for this character
                if (b >> 7) == 0:          # 0xxxxxxx → 1-byte
                    need = 0
                elif (b >> 5) == 0b110:    # 110xxxxx → 2-byte
                    need = 1
                elif (b >> 4) == 0b1110:   # 1110xxxx → 3-byte
                    need = 2
                elif (b >> 3) == 0b11110:  # 11110xxx → 4-byte
                    need = 3
                else:
                    # invalid leading byte
                    return False
            else:
                # must be a continuation byte: 10xxxxxx
                if (b >> 6) != 0b10:
                    return False
                need -= 1

        # characters must be complete
        return need == 0


# if __name__ == "__main__":
#     sol = Solution()
#     # quick manual check
#     print(sol.validUtf8([197, 130, 1]))   # True
#     print(sol.validUtf8([235, 140, 4]))   # False