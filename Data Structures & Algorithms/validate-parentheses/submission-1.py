class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranthesis_mapping = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        for c in s:
            if c in paranthesis_mapping.keys():
                if stack and stack[-1] == paranthesis_mapping[c]:
                    stack.pop()
                else:
                    return False
            else:    
                stack.append(c)
        return True if not stack else False
