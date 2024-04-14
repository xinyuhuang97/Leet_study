class Solution:
    def getdigit(self, nb, n):
        return nb // 10**n % 10
    
    def isHappy(self, n: int) -> bool:
        memo = set()
        
        while n!=1 and n not in memo:
            new_n = sum([int(c)**2 for c in str(n)])
            memo.add(n)
            n=new_n
        return True if n==1 else False
        
        