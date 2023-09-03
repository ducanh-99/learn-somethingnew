from typing import List
from heapq import heapify, heappush, heappop

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap = []
        sorted_pairs = list(zip(nums1, nums2))
        sorted_pairs.sort(key=lambda a:a[-1], reverse=True)
        res = total = 0
        for pair in sorted_pairs:
            num1, num2 = pair  
            heappush(heap, num1)
            total += num1
            if len(heap) > k:
                total -= heappop(heap)
            if len(heap) == k:
                res = max(res, total * num2)
        return res


s = Solution()
print(s.maxScore([1,3,3,2], [2,1,3,4], 3))
