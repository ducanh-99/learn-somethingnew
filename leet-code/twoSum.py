from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {} 
        for i in range(nums):
            if target - nums[i] in num_dict:
                return [num_dict[target-nums[i]], i ]
            else:
                num_dict[nums[i]] = i
        
        