class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = {}

        for i, val in enumerate(nums):
            if val in left:
                return [left[val], i]

            diff = target - val
            left[diff] = i

