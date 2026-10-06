class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)

        for num in nums:
            freq_dict[num] += 1
        
        heap_arr = []

        for num,freq in freq_dict.items():
            heapq.heappush(heap_arr, (freq,num))

            if(len(heap_arr) > k):
                heapq.heappop(heap_arr)
        
        return [num for freq,num in heap_arr]

        