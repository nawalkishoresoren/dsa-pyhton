class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix_mul = [1]*len(nums)
        result = [1]*len(nums)


        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix;
            prefix = prefix * nums[i]
        
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            suffix_mul[i] = suffix;
            suffix = suffix * nums[i]
            result[i] = result[i] * suffix_mul[i]
        
        return result

        
        