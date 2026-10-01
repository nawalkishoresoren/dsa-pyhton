class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        for num in nums:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1
        
        heap_arr = []

        for num, freq in frequency_dict.items():
            heapq.heappush(heap_arr,(freq,num))

            if(len(heap_arr)>k):
                heapq.heappop(heap_arr)
        
        return [num for freq,num in heap_arr]
        