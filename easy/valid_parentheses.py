class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paren_stack = []
        paren_str = "([{"
        
        for char in s:
            if char in paren_str:
                paren_stack.append(char)
            else:
                if len(paren_stack) < 1:
                    return False
                
                open_char = paren_stack.pop()
                
                if char == ")":
                    if open_char != "(":
                        return False
                elif char == "]":
                    if open_char != "[":
                        return False
                else:
                    if open_char != "{":
                        return False
        
        if len(paren_stack) == 0:
            return True
        else: 
            return False
