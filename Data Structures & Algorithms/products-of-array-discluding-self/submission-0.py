class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n
        result = [1]*n

        curr = 1
        for i in range(n):
            result[i] = curr
            curr *= nums[i]
        
        curr = 1
        for i in range(n-1,-1,-1):
            suffix[i] = curr
            curr *= nums[i]
            result[i] *= suffix[i]
        
        
        
        return result
        