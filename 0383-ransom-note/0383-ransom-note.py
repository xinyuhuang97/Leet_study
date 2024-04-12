from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters=defaultdict(int)  
        for s in magazine:
            magazine_letters[s]+=1
        for s in ransomNote:
            magazine_letters[s]-=1
            if magazine_letters[s]<0:
                return False
        return True