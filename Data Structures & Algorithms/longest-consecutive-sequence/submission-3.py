class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_streak = 0

        for num in nums:
            if num-1 not in seen:
                streak = 1
                while num+1 in seen:
                    streak += 1
                    num = num+1
                
                max_streak = max(max_streak,streak)
        
        return max_streak;
        