class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            anagram[key].append(word)
        
        return list(anagram.values())

        