class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            key = tuple(sorted(word))
            anagram[key] = anagram.get(key, []) + [word]
        return list(anagram.values())
            
            

        