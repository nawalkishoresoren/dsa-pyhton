class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx,num in enumerate(nums):
            new_target = target-num
            if new_target in seen:
                return [seen[new_target],idx]
            else:
                seen[num] = idx
        return [-1,-1]
        