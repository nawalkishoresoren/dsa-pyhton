class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        result = 0
        for num in nums:
            if num-1 not in seen:
                curr_num = num
                streak = 1
                while curr_num+1 in seen:
                    streak += 1
                    curr_num +=1
                result = max(result, streak)
        return result
                    
        