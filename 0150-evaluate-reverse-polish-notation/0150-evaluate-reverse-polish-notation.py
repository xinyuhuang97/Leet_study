ops={'/':(lambda x, y : x/y), '*':(lambda x, y : x*y), '+':(lambda x, y : x+y), '-':(lambda x, y : x-y) }
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c not in ['/', '*', '+', '-']:
                stack.append(c)
            else:
                y=int(stack.pop())
                x=int(stack.pop())
                stack.append(int(ops[c](x,y)))
        return int(stack[0])
        