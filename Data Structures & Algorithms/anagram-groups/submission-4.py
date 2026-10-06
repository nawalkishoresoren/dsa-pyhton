class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            freq_map[key].append(word)
        
        return list(freq_map.values())
        