class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right = 0,len(heights)-1
        max_water = -1

        while left<right:
            if heights[left]<=heights[right]:
                curr_water = (right-left) * heights[left]
                left += 1
                max_water = max(max_water,curr_water)
            else:
                curr_water = (right-left) * heights[right]
                right -= 1
                max_water = max(max_water,curr_water)

        return max_water