'''Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: " "
Explanation: There is no common prefix among the input strings.'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        else:
            first_prefix = strs[0]

        # Iterate over each string in the list, starting from the second string
        for s in strs[1:]:
            # Shorten the prefix until it matches the start of the current string
            while not s.startswith(first_prefix):
                first_prefix = first_prefix[:-1]
                # If prefix becomes empty, there’s no common prefix
                if not first_prefix:
                    return ""
        return first_prefix  # Return the longest common prefix

# Test the code
strs = ["dog","racecar","car"]
solution = Solution()
print(solution.longestCommonPrefix(strs))  # Output: " "
