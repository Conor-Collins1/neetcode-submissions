class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operands = ["+", "*", "-", "/"]
        

        for t in tokens:
            if t not in operands:
                stack.append(int(t))
            elif t == "+":
                stack [-2] = stack [-1] + stack [-2]
                stack.pop()
            elif t == "*":
                stack [-2] = stack [-1] * stack [-2]
                stack.pop()
            elif t == "-":
                stack [-2] = stack [-2] - stack [-1]
                stack.pop()
            elif t == "/":
                stack [-2] = int(stack [-2] / stack [-1])
                stack.pop()
        return int(stack[-1])
                

        