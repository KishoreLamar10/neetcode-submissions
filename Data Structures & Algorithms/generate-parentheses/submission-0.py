class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        result = []

        def backtrack(opend,closed):
            if opend == closed == n:
                result.append("".join(stack))
                return

            if opend < n:
                stack.append('(')
                backtrack(opend +  1, closed)
                stack.pop()

            if closed < opend:
                stack.append(')')
                backtrack(opend, closed+1)
                stack.pop()  
        
        backtrack(0,0)
        return result