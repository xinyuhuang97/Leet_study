class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        list_pos=[1,2,4,8,16,32,64,128,256]
        if n>1:
            if n%2 !=0 :
                return False
            else:
                if n>256:
                    return self.div_two(n/256)
                else:
                    return n in list_pos
        if n<1:
            return False
        return True

    
    def div_two(self,n):
        while n!=2 and n>2:
            n=n/2
        if n==2:
            return True
        return False

    
    
    