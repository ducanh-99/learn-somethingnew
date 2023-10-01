class Solution:

    def isHappy(self, n: int) -> bool:
        my_dict = {}
        while n not in my_dict:
            if n == 1:
                return True
            my_dict[n] = 1 
            print(str(n))
            n = sum([int(x)**2 for x in str(n)])
        return False

print(Solution().isHappy(2))