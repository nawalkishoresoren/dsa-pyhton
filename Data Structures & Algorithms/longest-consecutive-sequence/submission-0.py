class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        result = 0
        for num in nums:
            if num-1 not in seen:
                curr_num = num
                curr_streak = 1
                while curr_num+1 in seen:
                    curr_num += 1
                    curr_streak += 1
                result = max(result, curr_streak)
        
        return result