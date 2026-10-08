class Solution:
    def possible(self, speed:int, piles: List[int], h: int) -> bool:
        time = 0;
        for pile in piles:
            time += math.ceil(pile/speed)
        
        return True if time<=h else False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_Speed,max_Speed = 1,1
        for pile in piles:
            min_Speed = min(pile,min_Speed)
            max_Speed = max(pile,max_Speed)
        
        left, right = min_Speed, max_Speed

        result = max_Speed

        while(left<=right):
            speed = left + (right-left)//2

            if(self.possible(speed, piles,h)):
                result = speed
                right = speed-1
            else:
                left = speed + 1
        
        return result