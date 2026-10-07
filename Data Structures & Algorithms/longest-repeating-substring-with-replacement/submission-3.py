class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_dict = defaultdict(int)
        max_length = 0

        left = 0
        max_f = 0

        for right in range(len(s)):
            freq_dict[s[right]] += 1
            max_f = max(max_f, freq_dict[s[right]])

            if(right - left + 1) - max_f > k:
                freq_dict[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right-left+1)
        
        return max_length

