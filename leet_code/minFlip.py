"""
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.
"""


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a != 0 or b != 0 or c != 0:
            latest_a = a & 1
            latest_b = b & 1
            latest_c = c & 1
            if latest_c == 1:
                if latest_a == 0 and latest_b == 0:
                    res += 1
            else:
                res += (latest_a ^ 0) + (latest_b ^ 0)
            a = a >> 1
            b = b >> 1
            c = c >> 1
        return res
