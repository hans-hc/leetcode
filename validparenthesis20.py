class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in closeToOpen: #if this is a closing parenthesis
                #stack is not empty and value at the top of the stack is the matching opening parenthesis
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else: #if they dont match or if the stack is empty
                    return False
            else:
                stack.append(c)
        
        return not stack
        
