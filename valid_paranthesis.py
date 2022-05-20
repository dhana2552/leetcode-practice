# 20. Easy
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Input: s = "()"
# Output: true

# Input: s = "(]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {")":"(", "}":"{", "]":"["}
        for element in s:
            if element in hash_map:
                if stack and stack[-1] == hash_map[element]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(element)
        return True if not stack else False
