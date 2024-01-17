class Solution:
    def addBinary(self, a: str, b: str) -> str:
        print(bin(int(a, 2)) + bin(int(b, 2)))


Solution().addBinary(
    "11",
    "1"
)
