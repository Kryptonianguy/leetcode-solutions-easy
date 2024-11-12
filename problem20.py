'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true'''

class Solution:
    def isValid(self, s: str) -> bool:
        track_brackets = []
        brackets_pair = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
            }
        
        for char in s:
            if char in brackets_pair:
                track_brackets.append(char)
            
            elif char in brackets_pair.values():
                if not track_brackets or brackets_pair[track_brackets.pop()] != char:
                    return False
        
        return len(track_brackets) == 0

sol = Solution()
s = "()["
print(sol.isValid(s))