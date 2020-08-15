from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            if target - n in dic:
                return [i,dic[target-n]]
            dic[n] = i
        return [-1]
