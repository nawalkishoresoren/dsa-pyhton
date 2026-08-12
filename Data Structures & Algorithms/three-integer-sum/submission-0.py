class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            new_target = -nums[i]
            left,right = i+1,len(nums)-1
            while left<right:
                sum = nums[left] + nums[right]

                if sum == new_target:
                    result.append([nums[i],nums[left],nums[right]])

                    while(left<right and nums[left] == nums[left+1]):
                        left += 1
                    
                    while(left<right and nums[right] == nums[right-1]):
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif sum > new_target:
                    right -= 1
                else:
                    left += 1
        
        return result
        