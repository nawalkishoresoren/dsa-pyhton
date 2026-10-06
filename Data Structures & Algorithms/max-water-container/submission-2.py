class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left , right = 0, len(heights)-1
        max_water = -1

        while(left<right):
            if heights[left] <= heights[right]:
                curr_water = heights[left] * (right- left)
                max_water = max(max_water, curr_water)
                left += 1
            else:
                curr_water = heights[right] * (right- left)
                max_water = max(max_water, curr_water)
                right -= 1
        return max_water