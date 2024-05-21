class Solution:
    def isValid(self, s: str) -> bool:
        # Create a empty stack and a dictionary with keys as close parentheses and values as open parentheses 
        # Iteratate through the string and add to stack if open parentheses
        # Remove from stack if a close parentheses is present and it matches with the stack's top open parantheses
        # Else return False.        
        stack=list()
        matching_parens={')':'(', '}':'{', ']':'['}
        for paren in s:
            if paren in ['(', '{', '[']:
                stack.append(paren)
            else:
                if (stack==[]): return False
                if (matching_parens[paren] == stack[-1]): stack.pop()
                else: return False 
        if (stack==[]): return True
        else: return False